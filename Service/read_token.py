import os
import requests
from urllib.parse import quote

class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"OAuth {self.token}"
        }

    def upload_file(self, file_path, remote_path):
        """Загрузка файла на Яндекс.Диск под конкретным именем (без создания папок)."""
        # Проверка, существует ли локальный файл
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл {file_path} не существует.")
            return
        
        # Экранируем путь, чтобы избежать ошибок с пробелами или специальными символами
        encoded_remote_path = quote(remote_path)

        # URL для получения ссылки для загрузки файла
        upload_url = f"https://cloud-api.yandex.net/v1/disk/resources/upload?path={encoded_remote_path}&overwrite=true"
        
        try:
            # Получаем ссылку для загрузки файла
            response = requests.get(upload_url, headers=self.headers)
            response.raise_for_status()  # Бросает исключение при ошибке запроса

            href = response.json().get("href")
            if href:
                # Загружаем файл
                with open(file_path, "rb") as file_data:
                    upload_response = requests.put(href, files={"file": file_data})
                    upload_response.raise_for_status()  # Бросает исключение при ошибке загрузки

                print(f"Файл {file_path} успешно загружен на Яндекс.Диск в {remote_path}")
            else:
                print(f"Ошибка: Не удалось получить ссылку для загрузки файла. Ответ: {response.json()}")
        except requests.exceptions.RequestException as e:
            # Обработка ошибок запроса
            print(f"Ошибка при запросе к API Яндекс.Диска: {e}")
        except Exception as e:
            # Обработка других ошибок
            print(f"Не удалось загрузить файл {file_path} в облако: {e}")

# Пример использования
if __name__ == "__main__":
    token = 'y0_AgAAAAB1kl_bAAzlVQAAAAEbB9JkAACrn2txkx5OQYvR9QD1UBYOsym3Zw'  # Замените на ваш токен
    file_path = '/Users/nurken/Python-Practice/Service/file1.txt'  # Путь к локальному файлу
    remote_path = '/file1.txt'  # Путь на Яндекс.Диск (имя файла без создания папок)

    disk_service = YandexDisk(token)
    disk_service.upload_file(file_path, remote_path)
