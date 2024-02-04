from telebot import types
import polls

def get_main_menu():
    main_menu = types.ReplyKeyboardMarkup(True, True)
    main_menu.row('На главную', 'Опросы')
    main_menu.row('FAQ', "Обратная связь")
    main_menu.row('Материалы', "Контакты")
    return main_menu

def get_admin_menu():
    admin_menu = types.ReplyKeyboardMarkup(True, True)
    admin_menu.row('Отправить сообщение')
    admin_menu.row('Обратная связь*')
    admin_menu.row('Статистика опросов')
    return admin_menu

def get_topic_menu():
    topic_menu = types.InlineKeyboardMarkup()
    for topic in polls.get_topic():
        topic_menu.add(types.InlineKeyboardButton(topic, callback_data=topic))
    return topic_menu

def get_stats_menu():
    topic_menu = types.InlineKeyboardMarkup()
    for topic in polls.get_topic():
        topic_menu.add(types.InlineKeyboardButton(topic, callback_data="*"+topic))
    return topic_menu

def get_answer_menu(topic, number):
    answer_menu = types.InlineKeyboardMarkup()
    for answer in polls.get_answers(topic, number):
        answer_menu.add(types.InlineKeyboardButton(answer, callback_data=topic+":"+str(number)+":"+answer))
    return answer_menu
