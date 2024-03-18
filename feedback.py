import keyboards
from teleAPI import bot, cancel
import os
from telebot import types


path = "/root/sd/feedbacks"


def send_feedback(message):
    if not message.text in ["Текущий урок", "Коллекция уроков", "Посоветуй нас", "Расписание", "Библиотека", "Сдать задание", "Исследования", "Обратная связь"]:

        with open("/root/sd/feedbacks/{count}.txt".format(count=len(os.listdir(path)) + 1), 'w+', encoding="utf-8") as fileW:
            if message.chat.last_name != None:
                print(f"Отправитель: {message.chat.first_name} {message.chat.last_name}", file=fileW)
            else:
                print(f"Отправитель: {message.chat.first_name}", file=fileW)
            print(message.text, file=fileW)
        bot.send_message(message.chat.id, "Твое сообщение доставлено\n\nБлагодарим!", reply_markup=keyboards.get_main_menu())
    else:
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, "Отмена")
        return


def get(message):
    if len(os.listdir(path)) > 0:
        for gift in os.listdir(path):
            feedback_menu = types.InlineKeyboardMarkup()
            feedback_menu.add(types.InlineKeyboardButton(text="Удалить", callback_data="feedback_delete"))
            with open(f"/root/sd/feedbacks/{gift}", "r", encoding="utf-8") as fileR:
                bot.send_message(message.chat.id, fileR.read(), reply_markup=feedback_menu)
    else:
        bot.send_message(message.chat.id, "Новых пожеланий нет")


def remove(message):
    filepath = ""
    for feedback in os.listdir(path):
        with open(f"/root/sd/feedbacks/{feedback}", "r", encoding="utf-8") as fileR:
            if fileR.read() == message.text + '\n':
                filepath = fileR.name
        fileR.close()
    os.remove(filepath)

@bot.callback_query_handler(func=lambda call: call.data == "feedback_delete")
def callback_query(call):
    remove(call.message)
    bot.edit_message_text("Успешно", chat_id=call.message.chat.id, message_id=call.message.message_id)