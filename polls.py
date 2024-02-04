from teleAPI import bot
import keyboards
import os

poll_path = "C:/Users/smehn/PycharmProjects/SoundDesing/polls"
stats_path = "C:/Users/smehn/PycharmProjects/SoundDesing/stats"

def get_topic():
    topics = []
    if len(os.listdir(poll_path)) > 0:
        for poll in os.listdir(poll_path):
            topics.append(poll.rstrip('.txt'))
    return topics


def get_answers(topic, number):
    return get_quest(topic, number).split('=')[1].split('~')

def get_question(topic, number):
    return get_quest(topic, number).split('=')[0]

def get_quest(topic, number):
    with open(poll_path + "/" + topic + ".txt", "r") as file:
        return file.readlines()[number]


def start_polls(message):
    bot.send_message(message.chat.id, "Опросы", reply_markup=keyboards.get_topic_menu())

def poll(message, topic, number = 0):
    bot.edit_message_text(get_question(topic, number=number), message.chat.id, message.message_id, reply_markup=keyboards.get_answer_menu(topic=topic, number=number))

# напиши функцию, которая будет собирать статистику по вопросам и записывать в файл с названием темы в папке stats
def update_stats(topic, number, answer):
    answer = answer.rstrip('\n')
    # открываем файл с опросами
    with open(stats_path + "/" + topic + ".txt", "r") as f:
        # читаем все строки в список
        lines = f.readlines()

    # находим строку с нужным вопросом
    line = lines[number]
    # разбиваем строку по символу ~
    parts = line.split("~")
    # находим индекс нужного ответа
    index = [part.split("=")[0] for part in parts].index(answer)
    # увеличиваем счетчик для этого ответа на 1
    parts[index] = answer + "=" + str(int(parts[index].split("=")[1].rstrip("\n")) + 1)
    if index + 1 == len(parts):
        parts[index] += "\n"
    # соединяем список обратно в строку
    new_line = "~".join(parts)
    # заменяем старую строку на новую
    lines[number] = new_line

    # открываем новый файл для записи статистики
    with open(stats_path + "/" + topic + ".txt", "w") as f:
        # записываем каждую строку из списка
        for line in lines:
            f.write(line)

def get_stats(message, topic):
    with open(stats_path + "/" + topic + ".txt", "r") as f:
        bot.send_message(message.chat.id, f.read())
