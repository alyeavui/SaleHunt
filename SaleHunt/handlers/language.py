from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.menu import languages  # Проверь, что `languages` импортируется правильно

# Хэндлер для выбора языка
async def choose_language(message: types.Message):
    await message.answer("Выберите язык:", reply_markup=languages)

# Хэндлер для изменения языка
async def change_language(callback: types.CallbackQuery):
    lang = callback.data.split("_")[1]  # Получаем выбранный язык
    await callback.answer(f"Язык изменён на {lang}")

# Регистрация хэндлеров
def register_handlers_language(dp: Dispatcher):
    dp.register_message_handler(choose_language, lambda message: message.text == "🌍 Выбор языка")
    dp.register_callback_query_handler(change_language, Text(startswith="language_"))
