from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Привет 👋", "Помоги пж ❓"], ["жестко кринжани 😄", "Пока 👋"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привет! Я бот с кнопками. Выбери действие:", reply_markup=reply_markup
    )

# Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_text("здарова! Бродяга 😎(❁´◡`❁)")
    elif "помоги пж" in text:
        await update.message.reply_text("Вот что я могу:\n- Привет 👋\n- жестко кринжани 😄 \n- Прощай 👋")
    elif "жестко кринжани 😄" in text:
        await update.message.reply_text("job job job")
    elif "пока" in text:
        await update.message.reply_text("Ну и пошёл нафиг! 👋 Не в обиду,мы ещё свидимся!")
    else:
        await update.message.reply_text("ТЕБЕ ЧЁ НАДОО 😡😡😡")

# Основная функция запуска бота
def main():
    TOKEN = "8491526082:AAE6RkkNBmojT5BT9N4WeW_FFnbeFjOvNN0"

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()

