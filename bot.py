import telebot
from telebot import apihelper

# 1. Proxy ünvanınızı bura daxil edin (SOCKS5 və ya HTTP formatında)
# Məsələn: 'socks5://ip_ünvanı:port' və ya 'http://ip_ünvanı:port'
# Əgər şifrə tələb olunursa: 'socks5://istifadəçi:şifrə@ip_ünvanı:port'
apihelper.proxy = {
    'https': 'socks5://127.0.0.1:1080'  # Buranı öz proxy ünvanınızla əvəz edin
}

TOKEN = "9043788260:AAGmh_gxtWR-KGFCQwkQcGZj8a-BHyalbQE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! Proxy vasitəsilə bot uğurla qoşuldu! 🚀")

if __name__ == '__main__':
    print("Proxy üzərindən bot işləyir...")
    bot.infinity_polling()