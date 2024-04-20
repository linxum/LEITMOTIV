from teleAPI import bot, conn, get_current_lesson
import keyboards


def get_lesson_code(lesson: int):
    cursor = conn.cursor()
    cursor.execute("""SELECT code FROM home_codes WHERE work_id = %s;""", (lesson,))
    return cursor.fetchone()[0]

def home_work(message):
    if get_current_lesson(message) == 45:
        bot.send_message(message.chat.id, "Вы прошли все уроки!")
        return
    code = bot.send_message(message.chat.id, "Для открытия следующего урока, введи код, который предоставил преподаватель", reply_markup=keyboards.get_cancel_menu())
    bot.register_next_step_handler(code, check_code)

def check_code(message):
    if message.text in ["Текущий урок", "Коллекция уроков", "Посоветуй нас", "Расписание", "Библиотека", "Сдать задание", "Исследования", "Обратная связь"]:
        bot.clear_step_handler_by_chat_id(message.chat.id)
        bot.send_message(message.chat.id, "Отмена")
        return
    user_code = message.text.lower()
    lesson = get_current_lesson(message)
    code = get_lesson_code(lesson)
    if user_code == code:
        lesson = next_lesson(message, lesson)
        if lesson == 45:
            bot.send_message(message.chat.id, "Вы прошли все уроки!")
        else:
            bot.send_message(message.chat.id, "Вы перешли на следующий урок!")
        
    else:
        code = bot.send_message(message.chat.id, "Неправильный код. Попробуйте ещё раз", reply_markup=keyboards.get_cancel_menu())
        bot.register_next_step_handler(code, check_code)

def next_lesson(message, lesson):
    if 10 <= lesson <= 13:
        if lesson == 13:
            lesson = 21
        else:
            lesson = lesson + 1
    elif 20 <= lesson <= 28:
        if lesson == 28:
            lesson = 31
        else:
            lesson = lesson + 1
    elif 30 <= lesson <= 36:
        if lesson == 36:
            lesson = 41
        else:
            lesson = lesson + 1
    elif 40 <= lesson <= 44:
        if lesson == 44:
            lesson = 45
        else:
            lesson = lesson + 1
    cursor = conn.cursor()
    cursor.execute("""UPDATE current_work SET work_id = %s WHERE user_id = %s;""", (lesson, str(message.chat.id)))
    conn.commit()
    return lesson


def current_lesson(message):
    lesson = get_current_lesson(message)
    callback_functions[lesson](message)

def library_11(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_12(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_13(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_21(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_22(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_23(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_24(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_25(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_26(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_27(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_28(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_31(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_32(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_33(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_34(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_35(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_36(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_41(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_42(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_43(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_44(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

def library_45(message):
    msg = "Вы прошли все уроки!"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)

callback_functions = {
    11: library_11,
    12: library_12,
    13: library_13,
    21: library_21,
    22: library_22,
    23: library_23,
    24: library_24,
    25: library_25,
    26: library_26,
    27: library_27,
    28: library_28,
    31: library_31,
    32: library_32,
    33: library_33,
    34: library_34,
    35: library_35,
    36: library_36,
    41: library_41,
    42: library_42,
    43: library_43,
    44: library_44,
    45: library_45
}