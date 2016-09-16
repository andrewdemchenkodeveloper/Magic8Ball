import function as f

@f.bot.message_handler(commands=['start'])
def start(message):
    f.start(message)

@f.bot.message_handler(content_types=['text'])
def spin(message):
    f.main(message)

if __name__ == '__main__':
    f.bot.polling(none_stop=True)