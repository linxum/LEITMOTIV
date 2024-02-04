import keyboards
from teleAPI import bot
import os


path = "C:/Users/smehn/PycharmProjects/SoundDesing/feedbacks"

def start_feedback(message):
    message = bot.send_message(message.chat.id, "Напиши свои впечатления от нашего бота")
    bot.register_next_step_handler(message, send_feedback)

def send_feedback(message):
    with open("feedbacks/{count}.txt".format(count=len(os.listdir(path)) + 1), 'w+', encoding="utf-8") as fileW:
        if message.chat.last_name != None:
            print(f"Отправитель: {message.chat.first_name} {message.chat.last_name}", file=fileW)
        else:
            print(f"Отправитель: {message.chat.first_name}", file=fileW)
        print(message.text, file=fileW)
    bot.send_message(message.chat.id, "Твое сообщение доставлено)\n\nБлагодарим!", reply_markup=keyboards.get_main_menu())


def get(message):
    if len(os.listdir(path)) > 0:
        for gift in os.listdir(path):
            with open(f"feedbacks/{gift}", "r", encoding="utf-8") as fileR:
                bot.send_message(message.chat.id, fileR.read())
    else:
        bot.send_message(message.chat.id, "Новых пожеланий нет")


# def remove(message):
#     filepath = ""
#     for gift in os.listdir(path):
#         with open(f"gifts/{gift}", "r", encoding="utf-8") as fileR:
#             if fileR.read() == message.text + '\n':
#                 filepath = "C:/Users/smehn/PycharmProjects/SoundDesing/" + fileR.name
#         fileR.close()
#     os.remove(filepath)