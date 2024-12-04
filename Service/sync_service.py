import os
import time
import logging
import configparser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

config = configparser.ConfigParser()
config.read('config.ini')

try:
    local_folder = config.get('settings', 'local_folder')
    cloud_folder = config.get('settings', 'cloud_folder')
    access_token = config.get('settings', 'access_token')
    sync_interval = int(config.get('settings', 'sync_interval'))
    log_file = config.get('settings', 'log_file')
except configparser.NoSectionError as e:
    logging.error(f"Missing section in config file: {e}")
    raise
except configparser.NoOptionError as e:
    logging.error(f"Missing option in config file: {e}")
    raise

logging.basicConfig(filename=log_file, level=logging.INFO)

class SyncHandler(FileSystemEventHandler):
    def __init__(self, disk_service):
        self.disk_service = disk_service
    
    def on_modified(self, event):
        if event.is_directory:
            return
        logging.info(f"File modified: {event.src_path}")
        try:
            # Перезагружаем список файлов (без аргументов)
            self.disk_service.reload()
        except Exception as e:
            logging.error(f"Failed to reload: {e}")
    
    def on_created(self, event):
        if event.is_directory:
            return
        logging.info(f"File created: {event.src_path}")
        print(f"Attempting to upload file: {event.src_path}")
        try:
            # Загружаем файл на облако (здесь не должно быть src_path)
            self.disk_service.upload_file(event.src_path)
        except Exception as e:
            logging.error(f"Failed to upload file {event.src_path}: {e}")
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        logging.info(f"File deleted: {event.src_path}")
        try:
            self.disk_service.delete_file(event.src_path)
        except Exception as e:
            logging.error(f"Failed to delete file {event.src_path}: {e}")

def main():
    from yandex_disk_service import YandexDisk    
    
    if not os.path.exists(local_folder):
        logging.error(f"Local folder {local_folder} does not exist.")
        return
    
    disk_service = YandexDisk(access_token, cloud_folder)

    logging.info("Initial synchronization started.")
    try:
        # Первая синхронизация
        for filename in os.listdir(local_folder):
            file_path = os.path.join(local_folder, filename)
            disk_service.upload_file(file_path)
    except Exception as e:
        logging.error(f"Error during initial sync: {e}")
    
    event_handler = SyncHandler(disk_service)
    observer = Observer()
    observer.schedule(event_handler, path=local_folder, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(sync_interval)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
    