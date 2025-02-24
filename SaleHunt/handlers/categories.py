from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards.menu import categories, menu
from config import CATEGORIES
from handlers.discounts import show_discounts

async def show_categories(message: types.Message):
    await message.answer("Выбери категорию:", reply_markup=categories)

async def handle_category_selection(message: types.Message):
    await show_discounts(message)

async def go_back_to_menu(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=menu)

def register_handlers_categories(dp: Dispatcher):
    dp.register_message_handler(show_categories, lambda message: message.text == "🛍️ Категории скидок")
    dp.register_message_handler(handle_category_selection, lambda message: message.text in CATEGORIES)
    dp.register_message_handler(go_back_to_menu, lambda message: message.text == "🔙 Назад")
