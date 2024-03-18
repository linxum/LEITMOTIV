from teleAPI import bot
import keyboards
import os
import csv
from telebot import types

poll_path = "/root/sd/resources/polls.csv"

def get_topic():
    topics = []
    with open(poll_path, "r", encoding="utf-8") as file:
        r = csv.reader(file)
        for line in r:
            if line:
                topics.append(line[0])
    return topics


def start_polls(message):
    bot.send_message(message.chat.id, "Мы постоянно проводим исследования и учитываем ваше мнение для улучшения курса. Пожалуйста, примите участие в наших опросах.", reply_markup=keyboards.get_topic_menu())


def poll(message, topic):
    with open(poll_path, "r", encoding="utf-8") as file:
        r = csv.reader(file)
        for line in r:
            if line:
                if line[0] == topic:
                    poll_retry_menu = types.InlineKeyboardMarkup()
                    poll_retry_menu.add(types.InlineKeyboardButton(text="Ссылка на опрос", url=line[1]))
                    poll_retry_menu.add(types.InlineKeyboardButton(text="Пройти еще", callback_data="poll_retry"))
                    bot.edit_message_text(f"{line[2]}", message.chat.id, message.message_id, reply_markup=poll_retry_menu)


def add_topic(message):
    msg = bot.send_message(message.chat.id, "Название опроса (максимум 20 символов)")
    bot.register_next_step_handler(msg, add_link)

def add_link(message):
    msg = bot.send_message(message.chat.id, "Ссылка на опрос")
    bot.register_next_step_handler(msg, add_poll, message.text)

def add_poll(message, topic):
    with open(poll_path, "a", encoding="utf-8") as file:
        f = csv.writer(file, delimiter=",")
        f.writerow([topic, message.text])
        bot.send_message(message.chat.id, "Опрос успешно добавлен!", reply_markup=keyboards.get_admin_menu())

def delete_poll(message, topic):
    flag = False
    with open(poll_path, 'r', encoding='utf-8') as infile, open(poll_path + '.csv', 'w+', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[0] != topic:
                writer.writerow(row)
            else:
                flag = True

    os.replace(poll_path + '.csv', poll_path)
    if flag:
        bot.send_message(message.chat.id, "Успешно", reply_markup=keyboards.get_admin_menu())
    else:
        bot.send_message(message.chat.id, "Опрос не найден", reply_markup=keyboards.get_admin_menu())

@bot.callback_query_handler(func=lambda call: "poll" in call.data)
def callback_query(call):
    # опросы
    topics = get_topic()
    if call.data.split("_")[0] == "poll" and call.data.split("_")[1] in topics:
        poll(call.message, call.data.split("_")[1])
    elif call.data.split("_")[0] == "poll" and call.data.split("_")[1] == "delete" and call.data.split("_")[2] in topics:
        delete_poll(call.message, call.data.lstrip("poll_delete_"))
    elif call.data == "poll_retry":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start_polls(call.message)