from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.menu import menu  # Убедись, что menu импортируется правильно

# Хэндлер для команды /start
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который поможет тебе найти лучшие скидки!", reply_markup=menu)

# Хэндлер для кнопки "Назад"
async def go_back(callback: types.CallbackQuery):
    await callback.message.edit_text("Вы вернулись в главное меню", reply_markup=menu)

# Регистрация хэндлеров
def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_callback_query_handler(go_back, Text(equals="back"))
