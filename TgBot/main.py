from telebot import *

token = 'тут должен быть твой токен. Получить его можно в @BotFather'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Сложение")
    item2 = types.KeyboardButton("Вычитание")
    item3 = types.KeyboardButton("Умножение")
    item4 = types.KeyboardButton("Деление")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id,'Выберите операцию', reply_markup = markup)
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Сложение":
        a = bot.send_message(message.chat.id, "Введите 2 числа через пробел")
        bot.register_next_step_handler(a, summ)
    elif message.text == "Вычитание":
        a = bot.send_message(message.chat.id, "Введите 2 числа через пробел")
        bot.register_next_step_handler(a, minus)
    elif message.text == "Умножение":
        a = bot.send_message(message.chat.id, "Введите 2 числа через пробел")
        bot.register_next_step_handler(a, mult)
    elif message.text == "Деление":
        a = bot.send_message(message.chat.id, "Введите 2 числа через пробел")
        bot.register_next_step_handler(a, div)

def summ(message):
    try:
        res = str(message.text).split()
        bot.send_message(message.chat.id, float(res[0]) + float(res[1]))
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: Введите два числа.")
def minus(message):
    try:
        res = str(message.text).split()
        bot.send_message(message.chat.id, float(res[0]) - float(res[1]))
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: Введите два числа.")

def mult(message):
    try:
        res = str(message.text).split()
        bot.send_message(message.chat.id, float(res[0]) * float(res[1]))
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: Введите два числа.")
def div(message):
    try:
        res = str(message.text).split()
        num1 = float(res[0])
        num2 = float(res[1])
        if num2 != 0:
            bot.send_message(message.chat.id, num1 / num2)
        else:
            bot.send_message(message.chat.id, "На ноль делить нельзя.")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка: Введите два числа.")
    except ZeroDivisionError:
        bot.send_message(message.chat.id, "На ноль делить нельзя.")

bot.infinity_polling()