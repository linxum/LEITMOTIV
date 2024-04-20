from telebot import types
from teleAPI import conn, get_current_lesson
import psycopg2
import polls


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

def get_admin_menu():
    admin_menu = types.ReplyKeyboardMarkup(True, True)
    admin_menu.row('Отправить сообщение')
    admin_menu.row('Обратная связь*')
    admin_menu.row('Изменить опросы')
    admin_menu.row('Удалить пользователя')
    admin_menu.row('Режим пользователя')
    return admin_menu

def get_admin_polls_menu():
    polls_menu = types.ReplyKeyboardMarkup(True, True)
    polls_menu.row('Добавить опрос')
    polls_menu.row('Удалить опрос')
    return polls_menu

def get_topic_menu():
    topic_menu = types.InlineKeyboardMarkup()
    for topic in polls.get_topic():
        topic_menu.add(types.InlineKeyboardButton(topic, callback_data='poll_' + topic))
    return topic_menu

def get_delete_poll_menu():
    topic_menu = types.InlineKeyboardMarkup()
    for topic in polls.get_topic():
        topic_menu.add(types.InlineKeyboardButton(topic, callback_data="poll_delete_"+topic))
    return topic_menu

def get_cancel_menu():
    menu = types.InlineKeyboardMarkup()
    menu.add(types.InlineKeyboardButton("Отмена", callback_data="cancel"))
    return menu

def get_library_menu(message):
    library_menu = types.InlineKeyboardMarkup()
    count = get_current_lesson(message)
    if count // 10 >= 1:
        library_menu.add(types.InlineKeyboardButton("Ступень 1 / Введение", callback_data="library_1"))
    if count // 10 >= 2:
        library_menu.add(types.InlineKeyboardButton("Ступень 2 / Микс-инженерия", callback_data="library_2"))
    if count // 10 >= 3:
        library_menu.add(types.InlineKeyboardButton("Ступень 3 / Синтез", callback_data="library_3"))
    if count // 10 >= 4:
        library_menu.add(types.InlineKeyboardButton("Ступень 4 / Cаунд-дизайн", callback_data="library_4"))
    return library_menu

def get_materials_menu():
    library_menu = types.InlineKeyboardMarkup()
    library_menu.add(types.InlineKeyboardButton("Литература", callback_data="material_1"))
    library_menu.add(types.InlineKeyboardButton("ПО", callback_data="material_2"))
    library_menu.add(types.InlineKeyboardButton("Банки", callback_data="material_3"))
    return library_menu