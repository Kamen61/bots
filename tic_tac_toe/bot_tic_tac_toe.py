import telebot
import game

API_TOKEN = '5899153603:AAHs10vl9WXO1JEp2BseytmORro4drvscRQ'

bot = telebot.TeleBot(API_TOKEN)
row=''
line=''
char = 'X'
table= game.creat_array()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Игра началась !")
    begin(message)

def begin(message):
    bot.send_message(message.chat.id, game.print_array(table))
    bot.send_message(message.chat.id, f"Ходят '{char}'")
    bot.send_message(message.chat.id, "Введите столбец ")
    bot.register_next_step_handler(message, message_row)

@bot.message_handler(content_types='text')
def message_row(message):
    global row
    row= message.text
    bot.send_message(message.chat.id, "Введите строку")
    bot.register_next_step_handler(message, message_line)


@bot.message_handler(content_types='text')
def message_line(message):
    global line
    line= message.text
    global char
    game.start_game(row, line, table, char)
    if game.chek_win(table)== 'X' or game.chek_win(table)== 'O':
        bot.send_message(message.chat.id, f"Победил '{game.chek_win(table)}'")
    else:
        if char=='X':
            char = 'O'
        else:
            char='X'
        begin(message)
# bot.send_message(message.chat.id,row)


# @bot.message_handler(commands=['calc'])
# def calc_message(message):
#     bot.send_message(message.chat.id, "А теперь введите выражение" )
#
# @bot.message_handler(content_types='text')
# def message_reply(message):
#     # if
#     if pss.str_check(message.text):
#         result=eval(message.text)
#         lg.calcus_logger(result,message.text)
#         bot.send_message(message.chat.id, result)
#     else:
#         bot.send_message(message.chat.id, "Вы ввели неправильное выражение")
bot.polling()
