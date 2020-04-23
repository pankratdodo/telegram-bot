import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def start_message(mess):
    bot.send_message(mess.chat.id, "Привет, я бот Plettie", reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def send_text(message):
    chat_id = message.chat.id
    if message.text == 'Ты хороший бот':
        bot.send_message(chat_id, 'Спасибо:3', reply_markup=other_key(chat_id))
    elif message.text == 'Как дела?':
        bot.send_message(chat_id, 'Как обычно всё клубнично', reply_markup=other_key(chat_id))
    elif message.text == 'Пожалуйста' or message.text == 'пожалуйста':
        bot.send_message(chat_id, ' Другое дело!', reply_markup=keyboard())
    elif message.text == 'Привет' or message.text == 'привет':
        bot.send_message(chat_id, 'Привет, мой создатель', reply_markup=keyboard())
    elif message.text == 'Пока' or message.text == 'пока':
        bot.send_message(chat_id, 'Прощай, создатель', reply_markup=keyboard())
    elif message.text == "/help":
        bot.send_message(chat_id, "Напиши привет", reply_markup=keyboard())
    else:
        bot.send_message(chat_id, "Я тебя не понимаю. Напиши /help.", reply_markup=keyboard())

@bot.callback_query_handler(func=lambda message:True)
def ans(message):
    chat_id = message.message.chat.id
    if "button_one" in message.data:
        bot.send_message(chat_id, 'Круто, это кнопка 1')
    elif "button_two" in message.data:
        bot.send_message(chat_id, 'Круто, это кнопка 2')
    elif "button_three" in message.data:
        bot.send_message(chat_id, 'Круто, это кнопка 3')
    elif "button_return" in message.data:
        bot.send_message(chat_id, 'А пожалуйста?')

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Ты хороший бот')
    btn2 = types.KeyboardButton('Как дела?')
    markup.add(btn1, btn2)
    return markup

def other_key(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Ткни сюда', callback_data="button_one"))
    keyboard.add(types.InlineKeyboardButton(text='Или сюда', callback_data="button_two"))
    keyboard.add(types.InlineKeyboardButton(text='Можно даже тут', callback_data="button_three"))
    keyboard.add(types.InlineKeyboardButton(text='Уберите это', callback_data="button_return"))
    return keyboard

bot.polling(none_stop=True)
