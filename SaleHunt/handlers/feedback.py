from aiogram import types
from aiogram.dispatcher import Dispatcher

async def leave_feedback(message: types.Message):
    await message.answer("Отправьте свой отзыв сюда, и он будет передан администраторам.")

def register_handlers_feedback(dp: Dispatcher):
    dp.register_message_handler(leave_feedback, lambda message: message.text == "💬 Оставить отзыв")
