import os

class Config:
    # Токен Telegram-бота
    TELEGRAM_TOKEN = os.getenv('7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4')

    # Данные для базы данных или других сервисов, если нужно
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')

    # Параметры для напоминаний
    REMINDER_TIME = os.getenv('REMINDER_TIME', '08:00')  # Время напоминаний по умолчанию

    # Директория для логов
    LOGGING_DIR = os.getenv('LOGGING_DIR', 'logs')

    # Настройки для целей
    GOAL_NOTIFICATION_TIME = os.getenv('GOAL_NOTIFICATION_TIME', '09:00')  # Время для уведомлений о целях
    GOAL_PROGRESS_THRESHOLD = os.getenv('GOAL_PROGRESS_THRESHOLD', 50)  # Порог прогресса для уведомлений

    # Параметры API (если используются)
    API_KEY = os.getenv('API_KEY', 'your-api-key-here')

# Загружаем конфигурацию из файла .env, если такой существует
from dotenv import load_dotenv
load_dotenv()
