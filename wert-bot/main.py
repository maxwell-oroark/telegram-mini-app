from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

PARTNER_ID = "01HXW2J8YDH61DJR71JGRHGWTS"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "Open Mini App",
                web_app=WebAppInfo(
                    url=f"https://sandbox.wert.io/{PARTNER_ID}/widget/?click_id=34dc984f-1d0a-4b44-8ac4-5800d1401537&commodity=ETH&network=sepolia&commodities=%5B%7B%22commodity%22%3A%22ETH%22,%22network%22%3A%22sepolia%22%7D,%7B%22commodity%22%3A%22MATIC%22,%22network%22%3A%22amoy%22%7D%5D&widget_layout_mode=Modal&commodity_id=eth_sepolia.simple.ethereum"
                ),
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Click the button below to open the Mini App:", reply_markup=reply_markup
    )


def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("7068216248:AAGXH6d1z68PKW5dFkO4BFsIdWH8bZessmQ")
        .build()
    )

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    # application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
