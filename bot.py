from telegram import LabeledPrice, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    PreCheckoutQueryHandler,
    MessageHandler,
    CallbackContext,
    filters
)
import os

TOKEN = os.environ.get("8757534074:AAHDB5YQXNg0MKsQLbiEIjVYYwomRUrhKkU")
PROVIDER_TOKEN = os.environ.get("PROVIDER_TOKEN")  # токен Telegram Stars

PRICE_STARS = 250  # цена в Stars

# Стартовое сообщение
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        f"Привет, юный друг! Хочешь получить мануалы?\n"
        f"Тогда нужно оплатить {PRICE_STARS} Stars за доступ навсегда."
    )

# Команда покупки
async def buy(update: Update, context: CallbackContext):
    title = "Доступ к каналу"
    description = "Навсегда доступ к эксклюзивным мануалам"
    payload = "manual_access"
    currency = "XTR"  # Stars
    prices = [LabeledPrice("Доступ к каналу", PRICE_STARS)]
    
    await update.message.reply_invoice(
        title, description, payload, PROVIDER_TOKEN, currency, prices
    )

# Подтверждение перед оплатой
async def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    await query.answer(ok=True)

# После успешной оплаты
async def successful_payment_callback(update: Update, context: CallbackContext):
    # бот ничего не пишет
    pass

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback))

    app.run_polling()

if __name__ == "__main__":
    main()
