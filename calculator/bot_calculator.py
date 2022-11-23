import telebot
import processing_calculator as pss
import  logging_calculator as lg
API_TOKEN='5899153603:AAHs10vl9WXO1JEp2BseytmORro4drvscRQ'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")


@bot.message_handler(commands=['calc'])
def calc_message(message):
    bot.send_message(message.chat.id, "А теперь введите выражение" )

@bot.message_handler(content_types='text')
def message_reply(message):
    # if
    if pss.str_check(message.text):
        result=eval(message.text)
        lg.calcus_logger(result,message.text)
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "Вы ввели неправильное выражение")
bot.polling()
