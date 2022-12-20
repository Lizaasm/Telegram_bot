import random
import telebot

from telebot import types


bot = telebot.TeleBot("5733005167:AAHCBYZFqmJ-MjiY0T_ScmyOCOs1_QZ7mHQ")

with open("first.txt", "r", encoding='UTF-8') as f1:
    first = f1.readlines()
with open("second.txt", "r", encoding='UTF-8') as f2:
    second = f2.readlines()
with open("third.txt", "r", encoding='UTF-8') as f3:
    third = f3.readlines()
with open("fourth.txt", "r", encoding='UTF-8') as f4:
    fourth = f4.readlines()

f = open("advice1.txt", "r", encoding='UTF-8')
advice1 = f.read().split('\n')
f.close()


@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Гороскоп")
        item2=types.KeyboardButton("Совет")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nГороскоп для получения гороскопа на день\nСовет для получения мудрых слов ',  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Гороскоп":
        bot.send_message(message.from_user.id," {0.first_name}! \n Cейчас я расскажу тебе гороскоп на сегодня.".format(message.from_user))
        keyboard = types.InlineKeyboardMarkup()
        key_aries = types.InlineKeyboardButton(text='♈ Овен ♈', callback_data='zodiac')
        keyboard.add(key_aries)
        key_taurus = types.InlineKeyboardButton(text='♉ Телец ♉', callback_data='zodiac')
        keyboard.add(key_taurus)
        key_gemini = types.InlineKeyboardButton(text='♊ Близнецы ♊', callback_data='zodiac')
        keyboard.add(key_gemini)
        key_cancer = types.InlineKeyboardButton(text='♋ Рак ♋', callback_data='zodiac')
        keyboard.add(key_cancer)
        key_leo = types.InlineKeyboardButton(text='♌ Лев ♌', callback_data='zodiac')
        keyboard.add(key_leo)
        key_virgo = types.InlineKeyboardButton(text='♍ Дева ♍', callback_data='zodiac')
        keyboard.add(key_virgo)
        key_libra = types.InlineKeyboardButton(text='♎ Весы ♎', callback_data='zodiac')
        keyboard.add(key_libra)
        key_scorpio = types.InlineKeyboardButton(text='♏ Скорпион ♏', callback_data='zodiac')
        keyboard.add(key_scorpio)
        key_sagittarius = types.InlineKeyboardButton(text='♐ Стрелец ♐', callback_data='zodiac')
        keyboard.add(key_sagittarius)
        key_capricorn = types.InlineKeyboardButton(text='♑ Козерог ♑', callback_data='zodiac')
        keyboard.add(key_capricorn)
        key_aquarius = types.InlineKeyboardButton(text='♒ Водолей ♒', callback_data='zodiac')
        keyboard.add(key_aquarius)
        key_pisces = types.InlineKeyboardButton(text='♓ Рыбы ♓', callback_data='zodiac')
        keyboard.add(key_pisces)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    elif message.text.strip() == 'Совет':
        answer = random.choice(advice1)
    bot.send_message(message.chat.id, answer)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(third) + ' ' + random.choice(fourth)
        msg = msg.replace("\n", "")
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)