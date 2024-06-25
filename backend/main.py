from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler


def start(update, context):
    keyboard = [[InlineKeyboardButton("Open Mini App", url="https://your-app-url.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Click the button below to open the Mini App:", reply_markup=reply_markup
    )


def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
