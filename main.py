import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import os
from uvicorn import run  # این رو اینجا قرار بده

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TOKEN")

# تنظیمات لاگ
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# تعریف دستور start
async def start(update: Update, context):
    await update.message.reply_text("سلام! برای دریافت کد تخفیف شبانه، دکمه زیر را بزنید.")

# تعریف عملکرد دکمه
async def button(update: Update, context):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    await query.edit_message_text(text=f"تبریک! کد تخفیف شما: NIGHT1")

# تنظیمات سرور و اجرای برنامه
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    # اجرای برنامه روی پورت 10000
    run("main:app", host="0.0.0.0", port=10000)
