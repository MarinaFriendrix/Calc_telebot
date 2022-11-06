from telebot import types
import bot

def start(chatID):
    # Добавляем две кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("Рациональный")
    item2 = types.KeyboardButton("Комплексный")
    markup.add(item1)
    markup.add(item2)
    bot.bot.send_message(chatID, 'Выберите калькулятор:', reply_markup=markup)

def choice_message(chat_id, calc_type):
    bot.bot.send_message(chat_id, 'Вы выбрали ' + calc_type + ' калькулятор.')

def mes_input_real(chat_id, num):
    bot.bot.send_message(chat_id, 'Введите ' + num + ' число:')

def mes_input_real_part(chat_id, num):
    bot.bot.send_message(chat_id, 'Введите действительную часть ' + num + ' числа:')

def mes_input_i_part(chat_id, num):
    bot.bot.send_message(chat_id, 'Введите мнимую часть ' + num + ' числа:')

def mes_input_action(chat_id):
    bot.bot.send_message(chat_id, 'Введите действие:')

def view_data(chat_id, data, title):
    bot.bot.send_message(chat_id, str(title) + str(data))
