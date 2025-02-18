from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "7758438540:AAEB0jNcYvX6A7bNAf_qYqYxQCEaWv5Xko4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛍️ Категории скидок"))
menu.add(KeyboardButton("💬 Оставить отзыв"))
menu.add(KeyboardButton("🌍 Выбор языка"))

# Клавиатура с категориями скидок
categories = ReplyKeyboardMarkup(resize_keyboard=True)
categories.add(KeyboardButton("🥗 Еда"), KeyboardButton("👕 Одежда"))
categories.add(KeyboardButton("🏋️‍♂️ Спорт"), KeyboardButton("🔙 Назад"))

# Клавиатура с выбором языка
languages = ReplyKeyboardMarkup(resize_keyboard=True)
languages.add(KeyboardButton("🇰🇿 Қазақша"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
languages.add(KeyboardButton("🔙 Назад"))

# Кнопки для навигации по скидкам
navigation_buttons = InlineKeyboardMarkup()
navigation_buttons.add(InlineKeyboardButton("◀️", callback_data="prev"))
navigation_buttons.add(InlineKeyboardButton("▶️", callback_data="next"))

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который поможет тебе найти лучшие скидки!", reply_markup=menu)

# Кнопка "Категории скидок"
@dp.message_handler(lambda message: message.text == "🛍️ Категории скидок")
async def show_categories(message: types.Message):
    await message.answer("Выбери категорию:", reply_markup=categories)

# Кнопка "Назад"
@dp.message_handler(lambda message: message.text == "🔙 Назад")
async def back_to_menu(message: types.Message):
    await message.answer("Главное меню", reply_markup=menu)

# Кнопка "Оставить отзыв"
@dp.message_handler(lambda message: message.text == "💬 Оставить отзыв")
async def leave_feedback(message: types.Message):
    await message.answer("Отправьте свой отзыв сюда, и он будет передан администраторам.")

# Кнопка "Выбор языка"
@dp.message_handler(lambda message: message.text == "🌍 Выбор языка")
async def choose_language(message: types.Message):
    await message.answer("Выберите язык:", reply_markup=languages)

# Инлайн-кнопка "Подробнее"
@dp.callback_query_handler(lambda call: call.data == "more_info")
async def show_discount_details(call: types.CallbackQuery):
    await call.message.answer("🔹 Скидка 50% на доставку еды! Действует до 20 февраля.", reply_markup=navigation_buttons)

# Кнопки "Вперёд" и "Назад" для скидок
@dp.callback_query_handler(lambda call: call.data in ["prev", "next"])
async def navigate_discounts(call: types.CallbackQuery):
    if call.data == "prev":
        await call.message.answer("⬅️ Переход к предыдущей скидке...")
    else:
        await call.message.answer("➡️ Переход к следующей скидке...")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
