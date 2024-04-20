from teleAPI import bot, get_current_lesson
import keyboards
from telebot import types

library_back_button = types.InlineKeyboardMarkup()
library_back_button.add(types.InlineKeyboardButton("Назад", callback_data="library_back"))

materials_back_button = types.InlineKeyboardMarkup()
materials_back_button.add(types.InlineKeyboardButton("Назад", callback_data="material_back"))

library_1_list = ["-", "Физика звука, психоакустика", "Цифровой звук", "Функционал DAW"]
library_2_list = ["-", "Характеристики микса", "Урок 2", "Урок 3", "Урок 4", "Урок 5", "Урок 6", "Урок 7", "Урок 8"]
library_3_list = ["-", "Урок 1", "Урок 2", "Урок 3", "Урок 4", "Урок 5", "Урок 6"]
library_4_list = ["-", "Урок 1", "Урок 2", "Урок 3", "Урок 4"]

def start_library(message, back = False):
    if back:
        bot.edit_message_text("Доступ к новым урокам открывается после проверки вашего практического задания", message.chat.id, message.message_id, reply_markup=keyboards.get_library_menu(message))
    else:
        bot.send_message(message.chat.id, "Доступ к новым урокам открывается после проверки вашего практического задания", reply_markup=keyboards.get_library_menu(message))


def library_1(message):
    keys = types.InlineKeyboardMarkup()
    count = get_current_lesson(message)
    if count // 10 == 1:
        for i in range(1, min(count % 10 + 1, 4)):
            keys.add(types.InlineKeyboardButton(library_1_list[i], callback_data=f"library_1{i}"))
    else:
        for i in range(1, 4):
            keys.add(types.InlineKeyboardButton(library_1_list[i], callback_data=f"library_1{i}"))
    keys.add(types.InlineKeyboardButton("Назад", callback_data="library_back"))
    bot.edit_message_text("Задачи саунд-дизайнера. Основы Звукорежиссуры", message.chat.id, message.message_id, reply_markup=keys)

def library_11(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)
    

def library_12(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_13(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_2(message):
    keys = types.InlineKeyboardMarkup()
    count = get_current_lesson(message)
    if count // 10 == 2:
        for i in range(1, min(count % 10 + 1, 9)):
            keys.add(types.InlineKeyboardButton(library_2_list[i], callback_data=f"library_2{i}"))
    else:
        for i in range(1, 9):
            keys.add(types.InlineKeyboardButton(library_2_list[i], callback_data=f"library_2{i}"))
    keys.add(types.InlineKeyboardButton("Назад", callback_data="library_back"))
    bot.edit_message_text("Основы и логика сведения и мастеринга. [Смотреть](https://vk.com/@leitmotiv_edu-o-kurse) учебную программу.", message.chat.id, message.message_id,  parse_mode='Markdown', disable_web_page_preview=True, reply_markup=keys)

def library_21(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_22(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_23(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_24(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_25(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_26(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_27(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_28(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_3(message):
    keys = types.InlineKeyboardMarkup()
    count = get_current_lesson(message)
    if count // 10 == 3:
        for i in range(1, min(count % 10 + 1, 7)):
            keys.add(types.InlineKeyboardButton(library_3_list[i], callback_data=f"library_3{i}"))
    else:
        for i in range(1, 7):
            keys.add(types.InlineKeyboardButton(library_3_list[i], callback_data=f"library_3{i}"))
    keys.add(types.InlineKeyboardButton("Назад", callback_data="library_back"))
    bot.edit_message_text("Ступень 3 / Синтез", message.chat.id, message.message_id, reply_markup=keys)

def library_31(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_32(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_33(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_34(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_35(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_36(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_4(message):
    keys = types.InlineKeyboardMarkup()
    count = get_current_lesson(message)
    if count // 10 == 4:
        for i in range(1, min(count % 10 + 1, 5)):
            keys.add(types.InlineKeyboardButton(library_4_list[i], callback_data=f"library_4{i}"))
    else:
        for i in range(1, 5):
            keys.add(types.InlineKeyboardButton(library_4_list[i], callback_data=f"library_4{i}"))
    keys.add(types.InlineKeyboardButton("Назад", callback_data="library_back"))
    bot.edit_message_text("Ступень 4 / Cаунд-дизайн", message.chat.id, message.message_id, reply_markup=keys)

def library_41(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_42(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_43(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def library_44(message):
    msg = "Обучение начнется в ближайшее время. Все актуальные новости и объявления будут доступны в нашем паблике [ВКонтакте](https://vk.com/leitmotiv_edu)"
    bot.edit_message_text(msg, message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=library_back_button)

def start_materials(message, back=False):
    if back:
        bot.edit_message_text("Дополнительные материалы, связанные с курсом обучение.", message.chat.id, message.message_id, reply_markup=keyboards.get_materials_menu())
    else:
        bot.send_message(message.chat.id, "Дополнительные материалы, связанные с курсом обучение.", reply_markup=keyboards.get_materials_menu())

def materials_1(message):
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=materials_back_button)

def materials_2(message):
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=materials_back_button)

def materials_3(message):
    library_3_menu = types.InlineKeyboardMarkup()
    library_3_menu.add(types.InlineKeyboardButton("Семплы", callback_data="material_31"))
    library_3_menu.add(types.InlineKeyboardButton("Пресеты", callback_data="material_32"))
    library_3_menu.add(types.InlineKeyboardButton("Мультитреки", callback_data="material_33"))
    library_3_menu.add(types.InlineKeyboardButton("Назад", callback_data="material_back"))
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, reply_markup=library_3_menu)

def materials_31(message):
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=materials_back_button)

def materials_32(message):
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=materials_back_button)

def materials_33(message):
    bot.edit_message_text("Раздел будет пополняться по мере продвижения курса.", message.chat.id, message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=materials_back_button)

@bot.callback_query_handler(func=lambda call: call.data.split("_")[0] == "library" or call.data.split("_")[0] == "material")
def callback_query(call):
    if call.data == "library_1":
        library_1(call.message)
    elif call.data == "library_11":
        library_11(call.message)
    elif call.data == "library_12":
        library_12(call.message)
    elif call.data == "library_13":
        library_13(call.message)
    elif call.data == "library_2":
        library_2(call.message)
    elif call.data == "library_21":
        library_21(call.message)
    elif call.data == "library_22":
        library_22(call.message)
    elif call.data == "library_23":
        library_23(call.message)
    elif call.data == "library_24":
        library_24(call.message)
    elif call.data == "library_25":
        library_25(call.message)
    elif call.data == "library_26":
        library_26(call.message)
    elif call.data == "library_27":
        library_27(call.message)
    elif call.data == "library_28":
        library_28(call.message)
    elif call.data == "library_3":
        library_3(call.message)
    elif call.data == "library_31":
        library_31(call.message)
    elif call.data == "library_32":
        library_32(call.message)
    elif call.data == "library_33":
        library_33(call.message)
    elif call.data == "library_34":
        library_34(call.message)
    elif call.data == "library_35":
        library_35(call.message)
    elif call.data == "library_36":
        library_36(call.message)
    elif call.data == "library_4":
        library_4(call.message)
    elif call.data == "library_41":
        library_41(call.message)
    elif call.data == "library_42":
        library_42(call.message)
    elif call.data == "library_43":
        library_43(call.message)
    elif call.data == "library_44":
        library_44(call.message)
    elif call.data == "library_back":
        start_library(call.message, True)
    elif call.data == "material_1":
        materials_1(call.message)
    elif call.data == "material_2":
        materials_2(call.message)
    elif call.data == "material_3":
        materials_3(call.message)
    elif call.data == "material_31":
        materials_31(call.message)
    elif call.data == "material_32":
        materials_32(call.message)
    elif call.data == "material_33":
        materials_33(call.message)
    elif call.data == "material_back":
        start_materials(call.message, True)
