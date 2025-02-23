from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards.menu import help_menu  # Убедись, что help_menu импортируется правильно

# Хэндлер для команды "Помощь"
async def show_help(message: types.Message):
    await message.answer("Выбери действие:", reply_markup=help_menu)

# Хэндлер для команды "feedback" (отзыв)
async def feedback(message: types.Message):
    await message.answer("Напишите ваш отзыв, и он будет отправлен админу.")

# Хэндлер для обработки текста отзыва
async def send_feedback_to_admin(message: types.Message):
    admin_id = 123456789  # Здесь укажи ID админа
    await message.bot.send_message(admin_id, f"📩 Новый отзыв от {message.from_user.full_name}: {message.text}")
    await message.answer("✅ Ваш отзыв отправлен админу! Спасибо!")

# Регистрация хэндлеров
def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(show_help, lambda message: message.text == "ℹ️ Помощь")
    dp.register_message_handler(feedback, commands=['feedback'])
    dp.register_message_handler(send_feedback_to_admin, lambda message: message.text.startswith("Отзыв: "))
