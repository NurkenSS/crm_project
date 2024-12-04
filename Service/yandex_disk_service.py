import os
import time
import logging
import configparser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from yandex_disk_service import YandexDisk

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

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

class SyncHandler(FileSystemEventHandler):
    def __init__(self, disk_service):
        self.disk_service = disk_service
    
    def on_modified(self, event):
        if event.is_directory:
            return
        logging.info(f"Файл {event.src_path} обновлён в облаке.")
        try:
            self.disk_service.reload(event.src_path)
        except Exception as e:
            logging.error(f"Не удалось перезагрузить файл {event.src_path}: {e}")
    
    def on_created(self, event):
        if event.is_directory:
            return
        logging.info(f"Новый файл {event.src_path} загружен в облако.")
        try:
            self.disk_service.load(event.src_path)
        except Exception as e:
            logging.error(f"Не удалось загрузить файл {event.src_path}: {e}")
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        logging.info(f"Файл {event.src_path} удалён из облака.")
        try:
            self.disk_service.delete(event.src_path)
        except Exception as e:
            logging.error(f"Не удалось удалить файл {event.src_path}: {e}")

def main():
    logging.info(f"Начало работы программы. Папка для синхронизации: {local_folder}")
    
    if not os.path.exists(local_folder):
        logging.error(f"Папка {local_folder} не существует.")
        return
    
    disk_service = YandexDisk(access_token, cloud_folder)

    logging.info("Начало начальной синхронизации.")
    try:
        for filename in os.listdir(local_folder):
            file_path = os.path.join(local_folder, filename)
            disk_service.load(file_path)
    except Exception as e:
        logging.error(f"Ошибка при начальной синхронизации: {e}")
    
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
