from telegram import LabeledPrice, Update
from telegram.ext import Updater, CommandHandler, PreCheckoutQueryHandler, MessageHandler, CallbackContext, filters
import os

TOKEN = os.environ.get("8757534074:AAHDB5YQXNg0MKsQLbiEIjVYYwomRUrhKkU")  # токен бота
PROVIDER_TOKEN = os.environ.get("PROVIDER_TOKEN")  # токен Telegram Stars

PRICE_STARS = 250  # цена в Stars

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Привет, юный друг! Хочешь получить мануалы?\n"
        f"Тогда нужно оплатить {PRICE_STARS} Stars за доступ навсегда."
    )

def buy(update: Update, context: CallbackContext):
    title = "Доступ к каналу"
    description = "Навсегда доступ к эксклюзивным мануалам"
    payload = "manual_access"
    currency = "XTR"  # Telegram Stars
    prices = [LabeledPrice("Доступ к каналу", PRICE_STARS)]
    
    update.message.reply_invoice(
        title, description, payload, PROVIDER_TOKEN, currency, prices
    )

def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    query.answer(ok=True)

def successful_payment_callback(update: Update, context: CallbackContext):
    # ничего не пишет пользователю
    pass

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
