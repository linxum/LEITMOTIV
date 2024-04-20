from teleAPI import bot, conn

def delete_user(message):
    msg = bot.send_message(message.chat.id, "Напишите ID пользователя, которого хотите удалить")
    bot.register_next_step_handler(msg, delete_user_step)

def delete_user_step(message):
    user_id = message.text
    cursor = conn.cursor()
    try:
        cursor.execute("""DELETE FROM current_work WHERE user_id = %s;""", (user_id,))
        cursor.execute("""DELETE FROM refers WHERE friend_user_id = %s;""", (user_id,))
        cursor.execute("""DELETE FROM refers WHERE user_id = %s;""", (user_id,))
        cursor.execute("""DELETE FROM users WHERE user_id = %s;""", (user_id,))
        conn.commit()
        bot.send_message(message.chat.id, "Пользователь был удален")
        bot.send_message(int(user_id), "Твой аккаунт был удален")
    except:
        bot.send_message(message.chat.id, "Такого пользователя не существует")