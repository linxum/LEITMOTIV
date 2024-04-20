from telebot import types

import feedback
import polls
from teleAPI import bot, is_admin, cancel, is_subscribed, start, is_login
import keyboards
import lesson
import refer
import broadcast_message
import library
import admin
import begin_poll


@bot.message_handler(commands=['start'])
def com_start(message):
    broadcast_message.subscribe(message.chat.id)
    if is_admin(message.chat.id):
        bot.send_message(message.chat.id, "Hello Admin!", reply_markup=keyboards.get_admin_menu())
    else:
        if not is_subscribed(message.from_user.id):
            key_subscribe = types.ReplyKeyboardMarkup(True, True)
            key_subscribe.add("Проверить подписку")

            get_link = types.InlineKeyboardMarkup()
            get_link.add(types.InlineKeyboardButton(text="leitmotiv", url="https://t.me/leitmotiv_edu"))

            bot.send_message(message.chat.id, "Ссылка на канал", reply_markup=get_link)
            bot.send_message(message.chat.id, "Для работы с ботом вам необходимо подписаться на канал проекта",
                             reply_markup=key_subscribe)
        else:
            if begin_poll.check(message):
                start(message)
            else:
                begin_poll.start_poll(message)

@bot.message_handler(commands=['admin'])
def set_admin(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "Привет, админ!", reply_markup=keyboards.get_admin_menu())

@bot.message_handler(commands=['user'])
def set_user(message):
    if is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "Привет, юзер!", reply_markup=keyboards.get_main_menu())


@bot.callback_query_handler(func=lambda call: call.data == "cancel")
def callback_query(call):
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    bot.edit_message_text("Отменен", call.message.chat.id, call.message.message_id)
    

@bot.message_handler(content_types=['text'])
def com_text(message):
    if is_subscribed(message.from_user.id):
        if is_login(message.from_user.id):
            if message.text == "Проверить подписку":
                com_start(message)
            elif message.text == "Обратная связь":
                msg = bot.send_message(message.chat.id, "Обнаружили баг в боте или хотите предложить улучшения для курса? Пишите нам здесь!", reply_markup=keyboards.get_cancel_menu())
                bot.register_next_step_handler(msg, feedback.send_feedback)
            elif message.text == "Текущий урок":
                lesson.current_lesson(message)
            elif message.text == "Коллекция уроков":
                library.start_library(message)
            elif message.text == "Сдать задание":
                lesson.home_work(message)
            elif message.text == "Исследования":
                polls.start_polls(message)
            elif message.text == "Библиотека":
                library.start_materials(message)
            elif message.text == "Посоветуй нас":
                refer.show(message)
            elif message.text == "Отправить сообщение":
                if is_admin(message.chat.id):
                    broadcast_message.write_message(message)
            elif message.text == "Обратная связь*":
                if is_admin(message.chat.id):
                    feedback.get(message)
            elif message.text == "Изменить опросы":
                if is_admin(message.chat.id):
                    bot.send_message(message.chat.id, "Что вы хотите сделать?", reply_markup=keyboards.get_admin_polls_menu())
            elif message.text == "Добавить опрос":
                if is_admin(message.chat.id):
                    polls.add_topic(message)
            elif message.text == "Удалить опрос":
                if is_admin(message.chat.id):
                    bot.send_message(message.chat.id, "Что вы хотите удалить?", reply_markup=keyboards.get_delete_poll_menu())
            elif message.text == "Удалить пользователя":
                if is_admin(message.chat.id):
                    admin.delete_user(message)
            elif message.text == "Режим пользователя":
                bot.send_message(message.chat.id, "Режим пользователя", reply_markup=keyboards.get_main_menu())
        else:
            com_start(message)
    else:
        com_start(message)


bot.polling(none_stop=True)