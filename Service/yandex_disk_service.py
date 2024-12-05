import os
import requests

class YandexDisk:
    def __init__(self, token, cloud_folder):
        self.token = token
        self.cloud_folder = cloud_folder
        self.headers = {
            "Authorization": f"OAuth {self.token}"
        }

    def upload_file(self, file_path, remote_path):
        """Загрузка файла на Яндекс.Диск под конкретным именем."""
        upload_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={remote_path}&overwrite=true"
        
        response = requests.get(upload_url, headers=self.headers)
        
        if response.status_code == 200:
            href = response.json().get("href")
            if href:
                with open(file_path, "rb") as file_data:
                    upload_response = requests.put(href, files={"file": file_data})
                    if upload_response.status_code == 201:
                        print(f"Файл {file_path} успешно загружен на Яндекс.Диск в {remote_path}")
                    else:
                        print(f"Ошибка при загрузке файла: {upload_response.json()}")
            else:
                print(f"Ошибка: Не удалось получить ссылку для загрузки файла. Ответ: {response.json()}")
        else:
            print(f"Ошибка при получении URL для загрузки файла: {response.json()}")

    def load_file(self, file_path):
        """Загружает файл на Яндекс.Диск"""
        remote_path = os.path.join(self.cloud_folder, os.path.basename(file_path))
        self.upload_file(file_path, remote_path)

    def reload_file(self, file_path):
        """Обновляет файл на Яндекс.Диск"""
        remote_path = os.path.join(self.cloud_folder, os.path.basename(file_path))
        self.upload_file(file_path, remote_path)

    def delete_file(self, file_path):
        """Удаляет файл с Яндекс.Диска"""
        remote_path = os.path.join(self.cloud_folder, os.path.basename(file_path))
        delete_url = f"https://cloud-api.yandex.net/v1/disk/resources?path={remote_path}"
        response = requests.delete(delete_url, headers=self.headers)
        if response.status_code == 204:
            print(f"Файл {file_path} успешно удалён с Яндекс.Диска.")
        else:
            print(f"Ошибка при удалении файла: {response.json()}")
