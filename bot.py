import telebot

TOKEN = "9043788260:AAGmh_gxtWR-KGFCQwkQcGZj8a-BHyalbQE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Olimpiya 5 botu uğurla işə düşdü! 🚀")

if __name__ == '__main__':
    bot.infinity_polling()