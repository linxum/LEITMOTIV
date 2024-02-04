from teleAPI import bot

def subscribe(user_id):
    flag = False
    with open('resources/user_ids.txt', 'r+') as f:
        for line in f:
            if line == str(user_id) + '\n':
                flag = True

        if not flag:
            print(user_id, file=f)


# def unsubscribe(user_id, bot):
#     with open("resources/user_ids.txt", "r") as fR:
#         lines = fR.readlines()
#     with open("resources/user_ids.txt", 'w') as fW:
#         for line in lines:
#             if line.strip('\n') != str(user_id):
#                 fW.write(line)
#     bot.send_message(user_id, "Рассылка отключена. Для включения нужно использовать /start")


def write_message(message):
    message = bot.send_message(message.chat.id, "Write")
    bot.register_next_step_handler(message, send_message)


def send_message(message):
    with open('resources/user_ids.txt', 'r') as f:
        user_ids = f.readlines()
        for user_id in user_ids:
            bot.copy_message(user_id, message.chat.id, message.message_id)