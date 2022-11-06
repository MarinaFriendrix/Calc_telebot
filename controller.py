import bot
import view
import model
from fractions import Fraction

# Счетчик вводимых данных
inputCounter = -1

# Тип калькулятора. 0 - рациональный, 1 - комплексный.
calcType = 0

# числа
value_a = 0
value_b = 0

# части комплексного числа
a = 0
b = 0

def handle_mes(message):
    global inputCounter, calcType, value_a, value_b, a, b

    inputCounter += 1

    if message.text == "Рациональный":
        calcType = 0
    if message.text == "Комплексный":
        calcType = 1
    if message.text == "Рациональный" or message.text == "Комплексный":
        inputCounter = 0
        view.choice_message(message.chat.id, message.text)

    # inputCounter = 1, 2 - ввод первого числа
    if inputCounter == 0 and calcType == 0:
        view.mes_input_real(message.chat.id, "первое")
    if inputCounter == 0 and calcType == 1:
        view.mes_input_real_part(message.chat.id, "первого")
    if inputCounter == 1 and calcType == 1:
        view.mes_input_i_part(message.chat.id, "первого")

    if inputCounter == 1 and calcType == 0:
        value_a = Fraction(message.text)
        inputCounter += 1
    if inputCounter == 1 and calcType == 1:
        a = int(message.text)
    if inputCounter == 2 and calcType == 1:
        b = int(message.text)
        value_a = complex(a, b)
        view.view_data(message.chat.id, value_a, 'первое число: ')

    # inputCounter = 3, 4 - ввод второго числа
    if inputCounter == 2 and calcType == 0:
        view.mes_input_real(message.chat.id, "второе")
    if inputCounter == 2 and calcType == 1:
        view.mes_input_real_part(message.chat.id, "второго")
    if inputCounter == 3 and calcType == 1:
        view.mes_input_i_part(message.chat.id, "второго")

    if inputCounter == 3 and calcType == 0:
        value_b = Fraction(message.text)
        inputCounter += 1
    if inputCounter == 3 and calcType == 1:
        a = int(message.text)
    if inputCounter == 4 and calcType == 1:
        b = int(message.text)
        value_b = complex(a, b)
        view.view_data(message.chat.id, value_b, 'второе число: ')

    # inputCounter = 5 - запись чисел в модель, ввод действия
    if inputCounter == 4:
        model.init(value_a, value_b)
        view.mes_input_action(message.chat.id)

    # inputCounter = 6 - выполнение действия
    if inputCounter == 5:
        result = model.do_it(str(message.text))
        view.view_data(message.chat.id, result, "result = ")


    # bot.bot.send_message(message.chat.id, ' счетчик ввода: ' + str(inputCounter) + ', a=' + str(a) + ', b=' + str(b) + ', va=' + str(value_a) + ", vb=" + str(value_b))
    # bot.bot.send_message(message.chat.id, value_a)