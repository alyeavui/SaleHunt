from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from config import API_TOKEN
from handlers.start import register_handlers_start
from handlers.categories import register_handlers_categories
from handlers.help import register_handlers_help
from handlers.feedback import register_handlers_feedback
from handlers.language import register_handlers_language
from handlers.discounts import register_handlers_discounts

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_handlers_start(dp)
register_handlers_categories(dp)
register_handlers_help(dp)
register_handlers_feedback(dp)
register_handlers_language(dp)
register_handlers_discounts(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
