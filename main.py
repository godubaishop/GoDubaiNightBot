
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

# Token (from user)
TOKEN = "8053312481:AAGC8Z0FkFzaALzj6PWAS9_04IYCmrcTNjE"

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Storage for users and discount codes
claimed_users = []
max_users = 5
discount_codes = ["NIGHT1", "NIGHT2", "NIGHT3", "NIGHT4", "NIGHT5"]

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("دریافت کد تخفیف", callback_data='get_code')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! برای دریافت کد تخفیف شبانه دکمه زیر رو بزن:", reply_markup=reply_markup)

# Button handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id in claimed_users:
        await query.edit_message_text(text="شما قبلاً کد تخفیف دریافت کرده‌اید.")
    elif len(claimed_users) < max_users:
        code = discount_codes[len(claimed_users)]
        claimed_users.append(user_id)
        await query.edit_message_text(text=f"تبریک! شما جزو ۵ نفر اول هستید.
کد تخفیف شما: {code}")
    else:
        await query.edit_message_text(text="متأسفیم، ظرفیت ۵ نفر اول پر شده. منتظر پیشنهادهای ویژه بعدی باشید!")

# Main app
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == '__main__':
    main()
