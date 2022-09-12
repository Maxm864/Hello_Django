# 5756290776:AAGTZIEVAJ3Uy5IGC3VrHqJiVYHoXGN-ypY

import telebot
import random
from telebot import types

token='5756290776:AAGTZIEVAJ3Uy5IGC3VrHqJiVYHoXGN-ypY'
bot = telebot.TeleBot(token)

img_list = ['9-17.jpg', 'darzoves2.jpg']
img_path = random.choice(img_list)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Хочу пить", callback_data='1')
    eat_btn = types.InlineKeyboardButton(text="Хочу есть", callback_data='2')
    gukyat_btn = types.InlineKeyboardButton(text="Хочу гулять", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="Хочу спать'", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="Хочу шутку", callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(gukyat_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard=create_keyboard()
    bot.send_message(
        message.chat.id,
        "Добрый день! Выберите, что Вы хотите",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data=="1":
            img = open('9-17.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка воды",
                reply_markup=keyboard)
            img.close()
        if call.data == "2":
            img = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Картинка еда",
                reply_markup=keyboard)
            img.close()
        if call.data == "3":
            img = open('KK8.gif', 'rb')
            bot.send_video(
                chat_id=call.message.chat.id,
                video=img,
                caption="гуляю",
                reply_markup=keyboard)
            img.close()
        if call.data == "4":
            img = open('pMH.gif', 'rb')
            bot.send_video(
                chat_id=call.message.chat.id,
                video=img,
                caption="сплю",
                reply_markup=keyboard)
            img.close()
        if call.data == "5":
            # bot.send_photo(message.chat.id, photo=open(img_path, 'rb'))
            # img_path = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=open(img_path, 'rb'),
                caption="шутка",
                reply_markup=keyboard)
            img_path.close()


if __name__=="__main__":
    bot.polling(none_stop=True)