import telebot
import view
import controller

# Создаем экземпляр бота
bot = telebot.TeleBot('5620214884:AAE56ZvgVnLLwndWxZirIr73NYaij3xk204')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    view.start(m.chat.id)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    controller.handle_mes(message)

# Запускаем бота
bot.polling(none_stop=True, interval=0)