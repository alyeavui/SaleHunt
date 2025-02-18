from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, ApplicationBuilder

TOKEN = "7758438540:AAEB0jNcYvX6A7bNAf_qYqYxQCEaWv5Xko4"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я ваш Telegram-бот.")

async def echo(update: Update, context: CallbackContext):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

