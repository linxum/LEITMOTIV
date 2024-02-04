import telebot

import feedback
import polls
from teleAPI import bot, is_admin
import keyboards
import broadcast_message
import library


@bot.message_handler(commands=['start'])
def com_start(message):
    broadcast_message.subscribe(message.chat.id)
    if is_admin(message.chat.id):
        bot.send_message(message.chat.id, "Hello Admin!", reply_markup=keyboards.get_admin_menu())
    else:
        bot.send_message(message.chat.id, "Hello World!", reply_markup=keyboards.get_main_menu())

@bot.message_handler(commands=['admin'])
def set_admin(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "Привет, админ!", reply_markup=keyboards.get_admin_menu())

@bot.message_handler(commands=['user'])
def set_user(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "Привет, юзер!", reply_markup=keyboards.get_main_menu())

# def cancel(message):
#     bot.clear_step_handler_by_chat_id(message.chat.id)
#     if is_admin(message.from_user.id):
#         bot.send_message(message.chat.id, "Отмена", reply_markup=keyboards.admin_menu)
#     else:
#         bot.send_message(message.chat.id, "Отмена", reply_markup=keyboards.main_menu)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    topics = polls.get_topic()
    if call.data in topics:
        polls.poll(call.message, call.data)
    elif call.data.split(":")[0] in topics:
        polls.update_stats(call.data.split(":")[0], int(call.data.split(":")[1]), call.data.split(":")[2])
        try:
            if polls.get_quest(call.data.split(":")[0], int(call.data.split(":")[1])+1):
                polls.poll(call.message, call.data.split(":")[0], int(call.data.split(":")[1])+1)
        except IndexError:
            bot.edit_message_text("Вопросы закончились", call.message.chat.id, call.message.message_id)
    elif call.data.lstrip("*") in topics:
        polls.get_stats(call.message, call.data.lstrip("*"))


@bot.message_handler(content_types=['text'])
def com_text(message):
    if message.text == "На главную":
        # cancel(message)
        pass
    elif message.text == "Обратная связь":
        feedback.start_feedback(message)
    elif message.text == "FAQ":
        library.start_library(message)
    elif message.text == "Опросы":
        polls.start_polls(message)
    elif message.text == "Отправить сообщение":
        if is_admin(message.chat.id):
            broadcast_message.write_message(message)
    elif message.text == "Обратная связь*":
        if is_admin(message.chat.id):
            feedback.get(message)
    elif message.text == "Статистика опросов":
        if is_admin(message.chat.id):
            bot.send_message(message.chat.id, "Статистика опросов", reply_markup=keyboards.get_stats_menu())


bot.polling(none_stop=True)