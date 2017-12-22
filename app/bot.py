API_TOKEN = '371143473:AAE9YIDWoUOtj5uL7Fd6i4PcfPTMmfwO5So'
# WEBHOOK_HOST = 'localhost'
# WEBHOOK_PORT = 8443
# WEBHOOK_LISTEN = '0.0.0.0'
# WEBHOOK_SSL_CERT = './static/webhook_cert.pem'
# WEBHOOK_SSL_PRIV = './static/webhook_pkey.pem'
# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)
#
# host=WEBHOOK_LISTEN,
#     port=WEBHOOK_PORT,
#     ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
#     debug=True
from db_models import *
from telebot import TeleBot, types
bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=['all'])
def all_user(message):
    from db_models import User
    users = [str(user) for user in User.query.all()]
    sms = "\n".join(users)
    bot.send_message(message.chat.id, sms)



if __name__ == '__main__':
    bot.polling(none_stop=True)
