from teleAPI import bot, cancel, start, conn, generator
import csv
import time

def check(message):
    # with open("/root/sd/resources/stats.csv", "r", encoding="utf-8") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         if message.chat.id == int(row['id']):
    #             return True
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (str(message.chat.id),))
    if cursor.fetchone():
        return True
    return False

def start_poll(message):
    bot.send_message(message.chat.id, "Прежде чем приступить к работе с ботом, вам необходимо зарегистрироваться на курс. Чтобы сделать это - ответьте на следующие вопросы")
    time.sleep(1)
    age = bot.send_message(message.chat.id, "Твой возраст")
    bot.register_next_step_handler(age, set_city)

def set_city(message):
    try:
        age = int(message.text)
        city = bot.send_message(message.chat.id, "Твой город")
        bot.register_next_step_handler(city, set_univ, age)
    except:
        age = bot.send_message(message.chat.id, "Возраст должен быть числом")
        bot.register_next_step_handler(age, set_city)

def set_univ(message, age):
    univ = bot.send_message(message.chat.id, "Где ты учишься? Укажи учебное заведение и факультет или поставь прочерк, если не учишься в данный момент")
    bot.register_next_step_handler(univ, set_link, age, message.text)

def set_link(message, age, city):
    link = bot.send_message(message.chat.id, "Ссылка на страницу в VK.")
    bot.register_next_step_handler(link, set_refer, age, city, message.text)

def set_refer(message, age, city, univ):
    refer = bot.send_message(message.chat.id, "Если у тебя есть реферальный код - введи его, в противном случае поставь прочерк")
    bot.register_next_step_handler(refer, write, age, city, univ, message.text)

def write(message, age, city, univ, link):
    # result = {'id': message.chat.id, 'name': name, 'age': age, 'city': city}
    # with open("/root/sd/resources/stats.csv", "a", newline="\n", encoding="utf-8") as f:
    #     writer = csv.DictWriter(f, fieldnames=['id', 'name', 'age', 'city'])
    #     writer.writerow(result)
    code = generator.generate_random_number()
    cursor = conn.cursor()
    if message.text != '-':
        cursor.execute("""SELECT user_id FROM users WHERE refer_code = %s""", (message.text,))
        id = cursor.fetchone()
        if id is not None and id[0] is not None:
            cursor.execute("""
                        INSERT INTO users (user_id, link, city, age, university, refer_code, count_refer)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (message.chat.id, link, city, age, univ, code, 0))
            cursor.execute("""INSERT INTO current_work (user_id, work_id) VALUES (%s, %s)""", (message.chat.id, 11))
            cursor.execute("""INSERT INTO refers (user_id, friend_user_id) VALUES (%s, %s)""", (message.chat.id, id[0]))
            cursor.execute("""UPDATE users SET count_refer = count_refer + 1 WHERE user_id = %s""", (id[0],))
            
        else:
            msg = bot.send_message(message.chat.id, "Такого реферального кода не существует. Попробуй еще раз")
            bot.register_next_step_handler(msg, write, link, age, city, univ)
            return
    else:
        cursor.execute("""
                        INSERT INTO users (user_id, link, city, age, university, refer_code, count_refer)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (message.chat.id, link, city, age, univ, code, 0))
        cursor.execute("""INSERT INTO current_work (user_id, work_id) VALUES (%s, %s)""", (message.chat.id, 11))
    conn.commit()
    start(message)

# def print_user(message):
#     with open("/root/sd/resources/stats.csv", "r", encoding="utf-8") as f:
#         next(f)
#         reader = csv.DictReader(f)
#         for row in reader:
#             bot.send_message(message.chat.id, f"Имя: {row['name']}, возраст: {row['age']}, город: {row['city']}")