from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from handlers import add_habit, edit_habit, view_habits
import logging

API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Регистрация хендлеров
dp.register_message_handler(add_habit.start, commands="add_habit")
dp.register_message_handler(edit_habit.start, commands="edit_habit")
dp.register_message_handler(view_habits.show, commands="view_habits")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)