import telebot
from telebot import types
import psycopg2
import UniqueRandomGenerator

main_token = '<YOUR TOKEN>'
bot = telebot.TeleBot(main_token)

conn = psycopg2.connect(dbname='postgres', user='postgres',
                        password='0', host='localhost')

generator = UniqueRandomGenerator.UniqueRandomGenerator(1, 100000)

def get_main_menu():
    main_menu = types.ReplyKeyboardMarkup(True, True)
    main_menu.row('Текущий урок')
    main_menu.row('Коллекция уроков')
    main_menu.row("Посоветуй нас")
    main_menu.row("Сдать задание")
    main_menu.row('Библиотека')
    main_menu.row('Исследования')
    main_menu.row("Обратная связь")
    return main_menu

def get_current_lesson(message):
        cursor = conn.cursor()
        cursor.execute("""SELECT work_id FROM current_work WHERE user_id = %s;""", (str(message.chat.id),))
        return cursor.fetchone()[0]

def is_admin(user_id):
    with open('/root/sd/resources/admin_ids.txt', 'r+') as f:
        for line in f:
            if line == str(user_id) + '\n':
                return True
    return False


def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в бот!", reply_markup=get_main_menu())

def cancel(message, reply=False):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    if reply:
        bot.delete_message(message.chat.id, message.message_id - 2)
    bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=get_main_menu())


def is_subscribed(user_id, chat_id = "@leitmotiv_edu"):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        if member.status == 'left':
            return False
        else:
            return True
    except telebot.apihelper.ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False

def is_login(user_id):
    cursor = conn.cursor()
    cursor.execute("""SELECT user_id FROM users WHERE user_id = %s;""", (str(user_id),))
    return True if cursor.fetchone() else False