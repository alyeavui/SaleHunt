from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.menu import menu

async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который поможет тебе найти лучшие скидки!", reply_markup=menu)

async def go_back(message: types.Message):
    await message.answer("Вы вернулись в главное меню.", reply_markup=menu)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(go_back, Text(equals="🔙 Назад"))
