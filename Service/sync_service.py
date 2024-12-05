import os
import logging
import configparser
from yandex_disk_service import YandexDisk

# Чтение конфигурации
config = configparser.ConfigParser()
config.read('config.ini')

try:
    local_folder = config.get('settings', 'local_folder')
    cloud_folder = config.get('settings', 'cloud_folder')
    access_token = config.get('settings', 'access_token')
    log_file = config.get('settings', 'log_file')
except configparser.NoSectionError as e:
    logging.error(f"Missing section in config file: {e}")
    raise
except configparser.NoOptionError as e:
    logging.error(f"Missing option in config file: {e}")
    raise

# Настройка логирования
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Создаем логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def sync_file(file_path, cloud_path, disk_service):
    try:
        # Загрузка файла в облако
        disk_service.upload_file(file_path, cloud_path)
        logger.info(f"Файл {file_path} загружен в облако.")
        
        # Обновление файла в облаке
        disk_service.upload_file(file_path, cloud_path)  # Повторная загрузка для обновления
        logger.info(f"Файл {file_path} обновлён в облаке.")
        
        # Удаление файла из облака
        disk_service.delete_file(cloud_path)
        logger.info(f"Файл {file_path} удалён из облака.")
    except Exception as e:
        logger.error(f"Ошибка при синхронизации файла {file_path}: {e}")

def main():
    logger.info(f"Начало работы программы.")
    
    if not os.path.exists(local_folder):
        logger.error(f"Папка {local_folder} не существует.")
        return
    
    disk_service = YandexDisk(access_token, cloud_folder)

    # Синхронизация файла file1.txt
    file_path = os.path.join(local_folder, "file1.txt")
    cloud_path = file_path.replace(local_folder, cloud_folder)  # Путь для облака
    sync_file(file_path, cloud_path, disk_service)

if __name__ == "__main__":
    main()
