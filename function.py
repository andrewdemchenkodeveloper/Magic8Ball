import telebot
from telebot import types
import configuration
import random


bot = telebot.TeleBot(configuration.token)


def start(message):
    settings(message)


def answerEng(message):
    r = random.randint(1, 20)
    if (r == 1):
        a = 'It is certain'
    elif (r == 2):
        a = 'It is decidedly so'
    elif (r == 3):
        a = 'Without a doubt'
    elif (r == 4):
        a = 'Yes — definitely'
    elif (r == 5):
        a = 'You may rely on it'
    elif (r == 6):
        a = 'As I see it, yes'
    elif (r == 7):
        a = 'Most likely'
    elif (r == 8):
        a = 'Outlook good'
    elif (r == 9):
        a = 'Signs point to yes'
    elif (r == 10):
        a = 'Yes'
    elif (r == 11):
        a = 'Reply hazy, try again'
    elif (r == 12):
        a = 'Ask again later'
    elif (r == 13):
        a = 'Better not tell you now'
    elif (r == 14):
        a = 'Cannot predict now'
    elif (r == 15):
        a = 'Concentrate and ask again'
    elif (r == 16):
        a = 'Don’t count on it'
    elif (r == 17):
        a = 'My reply is no'
    elif (r == 18):
        a = 'My sources say no'
    elif (r == 19):
        a = 'Outlook not so good'
    elif (r == 20):
        a = 'Very doubtful'

    markup = types.ReplyKeyboardMarkup()
    answer = types.KeyboardButton('Get the answer')
    settings = types.KeyboardButton('Settings')
    author = types.KeyboardButton('Author')
    markup.row(answer)
    markup.row(settings)
    markup.row(author)
    bot.send_message(message.chat.id, a, reply_markup=markup)


def answerRus(message):
    r = random.randint(1, 20)
    if (r == 1):
        a = 'Бесспорно'
    elif (r == 2):
        a = 'Предрешено'
    elif (r == 3):
        a = 'Никаких сомнений'
    elif (r == 4):
        a = 'Определённо да'
    elif (r == 5):
        a = 'Можешь быть уверен в этом'
    elif (r == 6):
        a = 'Мне кажется — да'
    elif (r == 7):
        a = 'Вероятнее всего'
    elif (r == 8):
        a = 'Хорошие перспективы'
    elif (r == 9):
        a = 'Знаки говорят — да'
    elif (r == 10):
        a = 'Да'
    elif (r == 11):
        a = 'Пока не ясно, попробуй снова'
    elif (r == 12):
        a = 'Спроси позже'
    elif (r == 13):
        a = 'Лучше не рассказывать'
    elif (r == 14):
        a = 'Сейчас нельзя предсказать'
    elif (r == 15):
        a = 'Сконцентрируйся и спроси опять'
    elif (r == 16):
        a = 'Даже не думай'
    elif (r == 17):
        a = 'Мой ответ — нет'
    elif (r == 18):
        a = 'По моим данным — нет'
    elif (r == 19):
        a = 'Перспективы не очень хорошие'
    elif (r == 20):
        a = 'Весьма сомнительно'

    markup = types.ReplyKeyboardMarkup()
    answer = types.KeyboardButton('Получить ответ')
    settings = types.KeyboardButton('Настройки')
    author = types.KeyboardButton('Автор')
    markup.row(answer)
    markup.row(settings)
    markup.row(author)
    bot.send_message(message.chat.id, a, reply_markup=markup)


def settings(message):
    markup = types.ReplyKeyboardMarkup()
    eng = types.KeyboardButton('English')
    rus = types.KeyboardButton('Русский')
    markup.row(eng)
    markup.row(rus)
    bot.send_message(message.chat.id, 'Choose the language', reply_markup=markup)


def authorEng(message):
    engAuthorVar = 'Name:\nAndrew Demchenko\n\nSkill:\nJunior Python Developer\n\nE-Mail:\nandrewdemchenkodeveloper@gmail.com'
    bot.send_message(message.chat.id, engAuthorVar)


def authorRus(message):
    rusAuthorVar = 'Имя:\nАндрей Демченко\n\nНавык:\nJunior Python Developer\n\nE-Mail:\nandrewdemchenkodeveloper@gmail.com'
    bot.send_message(message.chat.id, rusAuthorVar)


def main(message):
    if (message.text in ['English', 'Get the answer']):
        answerEng(message)
    elif (message.text in ['Русский', 'Получить ответ']):
        answerRus(message)
    elif (message.text in ['Settings', 'Настройки']):
        settings(message)
    elif (message.text == 'Author'):
        authorEng(message)
    elif(message.text == 'Автор'):
        authorRus(message)



