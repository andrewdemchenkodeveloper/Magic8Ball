import telebot
from telebot import types
import configuration
import random


bot = telebot.TeleBot(configuration.token)


def start(message):
    settings(message)


def menuEng(message):
    markup = types.ReplyKeyboardMarkup()
    answer = types.KeyboardButton('Get the answer')
    settings = types.KeyboardButton('Settings')
    markup.row(answer)
    markup.row(settings)
    bot.send_message(message.chat.id, 'Ask a question', reply_markup=markup)


def answerEng(message):
    r = random.randint(1, 20)
    if (r == 1):
        bot.send_message(message.chat.id, 'It is certain')
    elif (r == 2):
        bot.send_message(message.chat.id, 'It is decidedly so')
    elif (r == 3):
        bot.send_message(message.chat.id, 'Without a doubt')
    elif (r == 4):
        bot.send_message(message.chat.id, 'Yes — definitely')
    elif (r == 5):
        bot.send_message(message.chat.id, 'You may rely on it')
    elif (r == 6):
        bot.send_message(message.chat.id, 'As I see it, yes')
    elif (r == 7):
        bot.send_message(message.chat.id, 'Most likely')
    elif (r == 8):
        bot.send_message(message.chat.id, 'Outlook good')
    elif (r == 9):
        bot.send_message(message.chat.id, 'Signs point to yes')
    elif (r == 10):
        bot.send_message(message.chat.id, 'Yes')
    elif (r == 11):
        bot.send_message(message.chat.id, 'Reply hazy, try again')
    elif (r == 12):
        bot.send_message(message.chat.id, 'Ask again later')
    elif (r == 13):
        bot.send_message(message.chat.id, 'Better not tell you now')
    elif (r == 14):
        bot.send_message(message.chat.id, 'Cannot predict now')
    elif (r == 15):
        bot.send_message(message.chat.id, 'Concentrate and ask again')
    elif (r == 16):
        bot.send_message(message.chat.id, 'Don’t count on it')
    elif (r == 17):
        bot.send_message(message.chat.id, 'My reply is no')
    elif (r == 18):
        bot.send_message(message.chat.id, 'My sources say no')
    elif (r == 19):
        bot.send_message(message.chat.id, 'Outlook not so good')
    elif (r == 20):
        bot.send_message(message.chat.id, 'Very doubtful')
    menuEng(message)


def menuRus(message):
    markup = types.ReplyKeyboardMarkup()
    answer = types.KeyboardButton('Получить ответ')
    settings = types.KeyboardButton('Настройки')
    markup.row(answer)
    markup.row(settings)
    bot.send_message(message.chat.id, 'Задай вопрос', reply_markup=markup)


def answerRus(message):
    r = random.randint(1, 20)
    if (r == 1):
        bot.send_message(message.chat.id, 'Бесспорно')
    elif (r == 2):
        bot.send_message(message.chat.id, 'Предрешено')
    elif (r == 3):
        bot.send_message(message.chat.id, 'Никаких сомнений')
    elif (r == 4):
        bot.send_message(message.chat.id, 'Определённо да')
    elif (r == 5):
        bot.send_message(message.chat.id, 'Можешь быть уверен в этом')
    elif (r == 6):
        bot.send_message(message.chat.id, 'Мне кажется — да')
    elif (r == 7):
        bot.send_message(message.chat.id, 'Вероятнее всего')
    elif (r == 8):
        bot.send_message(message.chat.id, 'Хорошие перспективы')
    elif (r == 9):
        bot.send_message(message.chat.id, 'Знаки говорят — да')
    elif (r == 10):
        bot.send_message(message.chat.id, 'Да')
    elif (r == 11):
        bot.send_message(message.chat.id, 'Пока не ясно, попробуй снова')
    elif (r == 12):
        bot.send_message(message.chat.id, 'Спроси позже')
    elif (r == 13):
        bot.send_message(message.chat.id, 'Лучше не рассказывать')
    elif (r == 14):
        bot.send_message(message.chat.id, 'Сейчас нельзя предсказать')
    elif (r == 15):
        bot.send_message(message.chat.id, 'Сконцентрируйся и спроси опять')
    elif (r == 16):
        bot.send_message(message.chat.id, 'Даже не думай')
    elif (r == 17):
        bot.send_message(message.chat.id, 'Мой ответ — нет')
    elif (r == 18):
        bot.send_message(message.chat.id, 'По моим данным — нет')
    elif (r == 19):
        bot.send_message(message.chat.id, 'Перспективы не очень хорошие')
    elif (r == 20):
        bot.send_message(message.chat.id, 'Весьма сомнительно')
    menuRus(message)


def settings(message):
    markup = types.ReplyKeyboardMarkup()
    eng = types.KeyboardButton('English')
    rus = types.KeyboardButton('Русский')
    markup.row(eng)
    markup.row(rus)
    bot.send_message(message.chat.id, 'Choose the language', reply_markup=markup)


def main(message):
    if (message.text == 'English'):
        menuEng(message)
    elif (message.text == 'Get the answer'):
        answerEng(message)
    elif (message.text == 'Русский'):
        menuRus(message)
    elif (message.text == 'Получить ответ'):
        answerRus(message)
    elif (message.text in ['Settings', 'Настройки']):
        settings(message)


