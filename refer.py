from teleAPI import conn, bot, cancel, get_current_lesson

def show(message):
    cursor = conn.cursor()
    cursor.execute("""SELECT refer_code, count_refer FROM users WHERE user_id = %s""", (str(message.chat.id),))
    result = cursor.fetchone()
    msg = f"За каждого друга, приглашенного тобой, ты получишь 1 балл, который можешь использовать для получения дополнительных бонусов. [Подробнее](https://clck.ru/39T3Sn)\n\nСкопируй свой личный код и отправь его другу или поделись в сторис\n\nТвой код: `{result[0]}`\n\nТвои баллы: {result[1]}"
    bot.send_message(message.chat.id, msg, parse_mode='Markdown', disable_web_page_preview=True)