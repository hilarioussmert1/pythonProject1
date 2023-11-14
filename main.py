import telebot
from config import keys, TOKEN
from utils import ConvertionException, CurrencyConventore

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_rules(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту с следущем формате:\n<Название валюты>\
<В какую валюту хотите перевести>\
<Количество переводимой валюты>\n Увидить список всех доступных валют можно увидеть написав роботу:/values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        qoute, base, amount = values
        total_base = CurrencyConventore.convert(qoute, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = (f'Цена {amount} {qoute} в {base} - {total_base}')
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)







