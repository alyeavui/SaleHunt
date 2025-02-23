from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import categories
from config import CATEGORIES

async def show_categories(message: types.Message):
    await message.answer("Выбери категорию:", reply_markup=categories)

def register_handlers_categories(dp: Dispatcher):
    dp.register_message_handler(show_categories, lambda message: message.text == "🛍️ Категории скидок")
