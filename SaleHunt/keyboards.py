from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("🛍️ Категории скидок"), KeyboardButton("ℹ️ Помощь"))

# Клавиатура с категориями скидок
categories = ReplyKeyboardMarkup(resize_keyboard=True)
categories.add(KeyboardButton("🥗 Еда"), KeyboardButton("👕 Одежда"))
categories.add(KeyboardButton("🏋️‍♂️ Спорт"), KeyboardButton("⬅️ Назад"))

# Клавиатура "Помощь"
help_menu = ReplyKeyboardMarkup(resize_keyboard=True)
help_menu.add(KeyboardButton("💬 Оставить отзыв"), KeyboardButton("🌍 Выбор языка"))
help_menu.add(KeyboardButton("📄 Доп. информация"), KeyboardButton("⬅️ Назад"))

# Клавиатура смены языка
languages = ReplyKeyboardMarkup(resize_keyboard=True)
languages.add(KeyboardButton("🇰🇿 Қазақша"), KeyboardButton("🇷🇺 Русский"), KeyboardButton("🇬🇧 English"))
languages.add(KeyboardButton("⬅️ Назад"))

# Кнопки навигации по скидкам
def get_discount_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    keyboard.add(InlineKeyboardButton("🔔 Подписаться", callback_data="subscribe"))
    return keyboard