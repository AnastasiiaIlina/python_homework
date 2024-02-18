import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from secret_data import TELEGRAM_BOT_TOKEN

keyboard = [
    [
        InlineKeyboardButton("Capricorn", callback_data="Capricorn"),
        InlineKeyboardButton("Virgo", callback_data="Virgo"),
        InlineKeyboardButton("Taurus", callback_data="Taurus"),
    ],
    [
        InlineKeyboardButton("Gemini", callback_data="Gemini"),
        InlineKeyboardButton("Aquarius", callback_data="Aquarius"),
        InlineKeyboardButton("Libra", callback_data="Libra"),
    ],
    [
        InlineKeyboardButton("Leo", callback_data="Leo"),
        InlineKeyboardButton("Aries", callback_data="Aries"),
        InlineKeyboardButton("Sagittarius", callback_data="Sagittarius"),
    ],
    [
        InlineKeyboardButton("Scorpio", callback_data="Scorpio"),
        InlineKeyboardButton("Pisces", callback_data="Pisces"),
        InlineKeyboardButton("Cancer", callback_data="Cancer"),
    ]
]


def get_daily_horoscope(sign: str) -> dict:
    """
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD)
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": "TODAY"}
    response = requests.get(url, params)

    return response.json()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Hi! Please choose your zodiac sign bellow:", reply_markup=reply_markup)

async def horoscope_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    await query.answer()

    api_response = get_daily_horoscope(query.data)

    await query.edit_message_text(text=f"Your horoscope data for {api_response["data"]["date"]}: {api_response["data"]["horoscope_data"]}")

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Enter /repeat command to choose another zodiac sign")

async def repeat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Want to get horoscope data for some one else? Choose zodiac sign bellow:", reply_markup=reply_markup)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    repeat_handler = CommandHandler('repeat', repeat)

    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(horoscope_button))
    application.add_handler(repeat_handler)
    
    application.run_polling()
