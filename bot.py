from telegram import LabeledPrice, Update
from telegram.ext import Updater, CommandHandler, PreCheckoutQueryHandler, MessageHandler, Filters, CallbackContext

TOKEN = "8757534074:AAHDB5YQXNg0MKsQLbiEIjVYYwomRUrhKkU"  # сюда вставь токен бота
PROVIDER_TOKEN = ""  # сюда вставь токен провайдера Telegram Stars через BotFather

PRICE_STARS = 300  # цена в Stars

# Стартовая команда
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет, юный друг! Хочешь получить мануалы?\n"
        f"Тогда нужно оплатить {PRICE_STARS} Stars за доступ навсегда."
    )

# Команда покупки
def buy(update: Update, context: CallbackContext):
    title = "Доступ к каналу"
    description = "Навсегда доступ к эксклюзивным мануалам"
    payload = "manual_access"
    currency = "XTR"  # Telegram Stars
    prices = [LabeledPrice("Доступ к каналу", PRICE_STARS)]
    
    update.message.reply_invoice(
        title, description, payload, PROVIDER_TOKEN, currency, prices
    )

# Подтверждение перед оплатой
def precheckout_callback(update: Update, context: CallbackContext):
    query = update.pre_checkout_query
    query.answer(ok=True)

# После успешной оплаты (не пишет пользователю)
def successful_payment_callback(update: Update, context: CallbackContext):
    # Здесь можно добавить выдачу доступа к каналу
    pass  # бот ничего не пишет

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    dp.add_handler(MessageHandler(Filters.successful_payment, successful_payment_callback))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
