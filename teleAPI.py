import telebot

main_token = '6765710167:AAHLpyOCdMTKKf9qipvW2JR2cLfy3A9lTVE'
bot = telebot.TeleBot(main_token)


def is_admin(user_id):
    with open('resources/admin_ids.txt', 'r+') as f:
        for line in f:
            if line == str(user_id) + '\n':
                return True
    return False
