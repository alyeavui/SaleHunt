from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛍️ Категории скидок"))
menu.add(KeyboardButton("ℹ️ Помощь"))

# Клавиатура с категориями скидок
categories = ReplyKeyboardMarkup(resize_keyboard=True)
categories.add(KeyboardButton("🥗 Еда"), KeyboardButton("👕 Одежда"))
categories.add(KeyboardButton("🏋️‍♂️ Спорт"), KeyboardButton("🔙 Назад"))

# Клавиатура для помощи
help_menu = ReplyKeyboardMarkup(resize_keyboard=True)
help_menu.add(KeyboardButton("💬 Оставить отзыв"), KeyboardButton("🌍 Выбор языка"))
help_menu.add(KeyboardButton("📄 Доп. информация"), KeyboardButton("🔙 Назад"))

# Клавиатура для выбора языка
languages = ReplyKeyboardMarkup(resize_keyboard=True)
languages.add(KeyboardButton("🇰🇿 Қазақша"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
languages.add(KeyboardButton("🔙 Назад"))

# Клавиатура подписки и возврата
def get_discount_keyboard(category):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔔 Подписаться", callback_data=f"subscribe_{category}"))
    keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data="back"))  # Добавляем кнопку назад
    return keyboard
