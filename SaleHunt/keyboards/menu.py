from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛍️ Категории скидок")).add(KeyboardButton("ℹ️ Помощь"))

categories = ReplyKeyboardMarkup(resize_keyboard=True)
categories.add(KeyboardButton("🥗 Еда"), KeyboardButton("👕 Одежда"))
categories.add(KeyboardButton("🏋️‍♂️ Спорт"), KeyboardButton("🔙 Назад"))

help_menu = ReplyKeyboardMarkup(resize_keyboard=True)
help_menu.add(KeyboardButton("💬 Оставить отзыв"), KeyboardButton("🌍 Выбор языка"))
help_menu.add(KeyboardButton("📄 Доп. информация"), KeyboardButton("🔙 Назад"))

languages = ReplyKeyboardMarkup(resize_keyboard=True)
languages.add(KeyboardButton("🇰🇿 Қазақша"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
languages.add(KeyboardButton("🔙 Назад"))

def get_discount_keyboard(category):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔔 Подписаться", callback_data=f"subscribe_{category}"))
    keyboard.add(InlineKeyboardButton("🔙 Назад", callback_data="back"))
    return keyboard
