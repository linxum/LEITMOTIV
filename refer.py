from teleAPI import conn, bot
from telebot import types

store_button = types.InlineKeyboardMarkup()
store_button.add(types.InlineKeyboardButton(text="В магазин", callback_data="store_start"))

def show(message):
    cursor = conn.cursor()
    cursor.execute("""SELECT refer_code, count_refer FROM users WHERE user_id = %s""", (str(message.chat.id),))
    result = cursor.fetchone()
    msg = f"За каждого друга, приглашенного тобой, ты получишь 10 балл, который можешь использовать для получения дополнительных бонусов. [Подробнее](https://clck.ru/39T3Sn)\n\nСкопируй свой личный код и отправь его другу или поделись в сторис\n\nТвой код: `{result[0]}`\n\nТвои баллы: {result[1]}"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=store_button)

@bot.callback_query_handler(func=lambda call: call.data.split("_")[0] == "store")
def callback_data(call):
    if call.data == "store_start":
        store = types.InlineKeyboardMarkup()
        store.add(types.InlineKeyboardButton(text="ZORGE & AYOPLUSH KIT", callback_data="store_confirm_1"))
        store.add(types.InlineKeyboardButton(text="AYOPLUSH 180+ ONESHOTS", callback_data="store_confirm_2"))
        bot.edit_message_text("Ознакомьтесь с предлагаемыми бонусами", call.message.chat.id, call.message.message_id, reply_markup=store)
    if call.data.split("_")[1] == "confirm":
        if call.data.split("_")[2] == "1":
            confirm = types.InlineKeyboardMarkup()
            confirm.add(types.InlineKeyboardButton(text="Подтвердить", callback_data="store_1"))
            confirm.add(types.InlineKeyboardButton(text="Отмена", callback_data="store_start"))
            bot.edit_message_text("ZORGE & AYOPLUSH KIT\n\nЦена - 15 баллов \n\nСодержит:\nВан-шоты - 70\nМиди - 15\nЛупы - 30\nМикс-пресеты - 10\n\nПревью: vk.cc/cvC7cO", call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=confirm)
        if call.data.split("_")[2] == "2":
            confirm = types.InlineKeyboardMarkup()
            confirm.add(types.InlineKeyboardButton(text="Подтвердить", callback_data="store_2"))
            confirm.add(types.InlineKeyboardButton(text="Отмена", callback_data="store_start"))
            bot.edit_message_text("AYOPLUSH 180+ ONESHOTS\n\nЦена - 30 баллов\n\nСодержит: \nBASS - 76\nKEYS - 19\nPAD - 5\nSYNTH - 81\n\nПревью: vk.cc/cvsRw7", call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=confirm)
    if call.data.split("_")[1] == '1':
        cursor = conn.cursor()
        cursor.execute("""SELECT count_refer FROM users WHERE user_id = %s""", (str(call.message.chat.id),))
        result = cursor.fetchone()
        if result[0] >= 15:
            cursor.execute("""UPDATE users SET count_refer = count_refer - 15 WHERE user_id = %s""", (str(call.message.chat.id),))
            bot.edit_message_text("Ваш подарок за 15 баллов\n\nТекущий баланс: " + str(result[0] - 15), call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=True)
            conn.commit()
        else:
            bot.edit_message_text("Ты не можете купить, поскольку у тебя не хватает баллов", call.message.chat.id, call.message.message_id, reply_markup=store_button)
    if call.data.split("_")[1] == '2':
        cursor = conn.cursor()
        cursor.execute("""SELECT count_refer FROM users WHERE user_id = %s""", (str(call.message.chat.id),))
        result = cursor.fetchone()
        if result[0] >= 30:
            cursor.execute("""UPDATE users SET count_refer = count_refer - 30 WHERE user_id = %s""", (str(call.message.chat.id),))
            bot.edit_message_text("Ваш подарок за 30 баллов\n\nТекущий баланс: " + str(result[0] - 30), call.message.chat.id, call.message.message_id, parse_mode='Markdown', disable_web_page_preview=True)
            conn.commit()
        else:
            bot.edit_message_text("Ты не можете купить, поскольку у тебя не хватает баллов", call.message.chat.id, call.message.message_id, reply_markup=store_button)