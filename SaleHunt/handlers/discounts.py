from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import get_discount_keyboard
from config import DISCOUNTS, USER_SUBSCRIPTIONS

async def show_discounts(message: types.Message):
    category = message.text
    if category in DISCOUNTS:
        discounts = DISCOUNTS[category]
        if discounts:
            for discount in discounts:
                await message.answer(discount, reply_markup=get_discount_keyboard())
        else:
            await message.answer("Пока нет актуальных скидок в этой категории.")
    else:
        await message.answer("Выберите категорию скидок из меню.")

async def subscribe(call: types.CallbackQuery):
    user_id = call.from_user.id
    category = call.message.text.split("\n")[0]  # Категория из сообщения
    if user_id not in USER_SUBSCRIPTIONS:
        USER_SUBSCRIPTIONS[user_id] = []
    if category not in USER_SUBSCRIPTIONS[user_id]:
        USER_SUBSCRIPTIONS[user_id].append(category)
        await call.message.answer(f"✅ Вы подписались на скидки в категории {category}!")
    else:
        await call.message.answer("Вы уже подписаны на эту категорию.")

def register_handlers_discounts(dp: Dispatcher):
    dp.register_message_handler(show_discounts, lambda message: message.text in DISCOUNTS.keys())
    dp.register_callback_query_handler(subscribe, lambda call: call.data == "subscribe")