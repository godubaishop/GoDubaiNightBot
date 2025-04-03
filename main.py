from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import logging
import os
from uvicorn import run

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")

# تنظیمات لاگ
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# تعریف دستور start
async def start(update, context):
    await update.message.reply_text("سلام!")

# تعریف عملکرد دکمه
async def button(update, context):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    await query.edit_message_text(text=f"User ID: {user_id}")

# تعریف اپلیکیشن و اجرا
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
