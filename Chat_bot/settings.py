import os

# Токен для вашего Telegram бота
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7678163374:AAHy-xfKIXgZYqzzydzkearFYbq5Xzi9kO4")

# Настройки базы данных (если необходимо)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
# Если используете PostgreSQL:
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Прочие настройки
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
