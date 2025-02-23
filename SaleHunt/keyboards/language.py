from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для выбора языка
languages = ReplyKeyboardMarkup(resize_keyboard=True)
languages.add(KeyboardButton("🇰🇿 Қазақша"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
languages.add(KeyboardButton("🔙 Назад"))
