from aiogram import Bot
import asyncio

TOKEN = "7758438540:AAEB0jNcYvX6A7bNAf_qYqYxQCEaWv5Xko4"

async def test_connection():
    try:
        bot = Bot(token=TOKEN)
        user = await bot.get_me()
        print(f"✅ Бот работает! Имя: {user.first_name}, Username: @{user.username}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        await bot.session.close()  # Закрываем соединение

if __name__ == "__main__":
    asyncio.run(test_connection())
