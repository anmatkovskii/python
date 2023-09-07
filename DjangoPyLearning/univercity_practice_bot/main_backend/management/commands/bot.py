import json
import telebot
from telebot import types
from datetime import date, datetime
from operator import itemgetter
import requests

config = {
    'name': 'Task Manager Bot',
    'token': '5995978139:AAF3BhvS9pRKpSK3eRlItdosQSGpjPKwAyc'
}

reg_buttons = telebot.types.InlineKeyboardMarkup()
reg_buttons.add(telebot.types.InlineKeyboardButton(text="Login", callback_data="Login"))
reg_buttons.add(telebot.types.InlineKeyboardButton(text="New here? Register!", callback_data="Register"))

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Show previous tasks")
button2 = types.KeyboardButton("Show current tasks")
button3 = types.KeyboardButton("Show future tasks")
keyboard.add(button1, button2, button3)

bot = telebot.TeleBot(config["token"])


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome! You need to be authorized to access bot's functions",
                     reply_markup=reg_buttons)


@bot.callback_query_handler(func=lambda call: call.data in ('Login', 'Register', 'Back'))
def reg_login(call):
    if call.data == "Login":
        username = bot.send_message(call.from_user.id, 'Enter your username')
        bot.register_next_step_handler(username, login)
    elif call.data == "Register":
        username = bot.send_message(call.from_user.id, 'Create a username')
        bot.register_next_step_handler(username, reg)
    elif call.data == "Back":
        bot.send_message(call.from_user.id, "You need to be authorized to access bot's functions",
                         reply_markup=reg_buttons)
    else:
        bot.send_message(call.from_user.id, 'Error')


def login(message):
    try:
        url = "http://127.0.0.1:8000/main/users/"
        json_list = requests.get(url).json()
        counter = 0
        username = message.text
        for i in json_list:
            if i['username'] == username:
                counter += 1
        if counter == 1:
            password = bot.send_message(message.chat.id, "User found. Now enter your password!")

            def password_check(message):
                back_to_login = telebot.types.InlineKeyboardMarkup()
                back_to_login.add(telebot.types.InlineKeyboardButton(text="Back to login", callback_data="Back"))
                for i in json_list:
                    if i['username'] == username and i['password'] == message.text:
                        func = bot.send_message(message.chat.id, "Login successful! Functions unlocked "
                                                                 "(open command keyboard)", reply_markup=keyboard)

                        @bot.message_handler(content_types=['text'])
                        def task_functions(message):
                            url_users = "http://127.0.0.1:8000/main/users/"
                            url_tasks = "http://127.0.0.1:8000/main/tasks/"
                            json_users_list = requests.get(url_users).json()
                            json_tasks_list = requests.get(url_tasks).json()
                            user_tg_id = message.from_user.id
                            accept_decline = telebot.types.InlineKeyboardMarkup()
                            accept_decline.add(
                                telebot.types.InlineKeyboardButton(text="Decline task", callback_data="Task Decline"))
                            accept_decline.add(
                                telebot.types.InlineKeyboardButton(text="Accept task", callback_data="Task Accept"))
                            if message.text == "Show future tasks":
                                task_counter = 0
                                for i in json_users_list:
                                    if i['userTelegramId'] == user_tg_id:
                                        user_id = i['id']
                                        for j in json_tasks_list:
                                            if j['userID_id'] == user_id:
                                                if (j['startTime']).replace('T', ' ').replace('Z', '') > str(
                                                        datetime.now()):
                                                    task = f"Task Name: {j['taskName']}\n\n" \
                                                           f"Description: {j['taskDescription']}\n\n" \
                                                           f"Begins: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
                                                           f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
                                                           f"Status: {j['done']}"
                                                    task_counter += 1
                                                    if j['done'] != "In Process":
                                                        bot.send_message(message.chat.id, task,
                                                                         reply_markup=accept_decline)

                                                        @bot.callback_query_handler(
                                                            func=lambda call: call.data.startswith('Task'))
                                                        def task_status(call):
                                                            if call.data == "Task Decline":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'Declined'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                            elif call.data == "Task Accept":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'In Process'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                    else:
                                                        bot.send_message(message.chat.id, task)
                                                    if task_counter == 0:
                                                        bot.send_message(message.chat.id, "You have no future tasks",
                                                                         reply_markup=keyboard)
                                bot.send_message(message.chat.id,
                                                 "Please, accept or decline tasks if you haven't done "
                                                 "it yet ☝", reply_markup=keyboard)
                            elif message.text == "Show current tasks":
                                task_counter = 0
                                for i in json_users_list:
                                    if i['userTelegramId'] == user_tg_id:
                                        user_id = i['id']
                                        for j in json_tasks_list:
                                            if j['userID_id'] == user_id:
                                                if (j['startTime']).replace('T', ' ').replace('Z', '') < str(
                                                        datetime.now()) \
                                                        < (j['endTime']).replace('T', ' ').replace('Z', ''):
                                                    task = f"Task Name: {j['taskName']}\n\n" \
                                                           f"Description: {j['taskDescription']}\n\n" \
                                                           f"Began: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
                                                           f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
                                                           f"Status: {j['done']}"
                                                    task_counter += 1
                                                    if j['done'] != "In Process":
                                                        bot.send_message(message.chat.id, task,
                                                                         reply_markup=accept_decline)

                                                        @bot.callback_query_handler(
                                                            func=lambda call: call.data.startswith('Task'))
                                                        def task_status(call):
                                                            if call.data == "Task Decline":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'Declined'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                            elif call.data == "Task Accept":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'In Process'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                    else:
                                                        bot.send_message(message.chat.id, task)
                                                    if task_counter == 0:
                                                        bot.send_message(message.chat.id, "You have no current tasks",
                                                                         reply_markup=keyboard)
                                bot.send_message(message.chat.id,
                                                 "Please, accept or decline tasks if you haven't done "
                                                 "it yet ☝", reply_markup=keyboard)
                            elif message.text == "Show previous tasks":
                                task_counter = 0
                                for i in json_users_list:
                                    if i['userTelegramId'] == user_tg_id:
                                        user_id = i['id']
                                        for j in json_tasks_list:
                                            if j['userID_id'] == user_id:
                                                if str(datetime.now()) > (j['endTime']).replace('T', ' ').replace('Z',
                                                                                                                  ''):
                                                    task = f"Task Name: {j['taskName']}\n\n" \
                                                           f"Description: {j['taskDescription']}\n\n" \
                                                           f"Began: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
                                                           f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
                                                           f"Status: {j['done']}"
                                                    task_counter += 1
                                                    if j['done'] != "In Process":
                                                        bot.send_message(message.chat.id, task,
                                                                         reply_markup=accept_decline)

                                                        @bot.callback_query_handler(
                                                            func=lambda call: call.data.startswith('Task'))
                                                        def task_status(call):
                                                            if call.data == "Task Decline":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'Declined'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                            elif call.data == "Task Accept":
                                                                data = {'taskName': j['taskName'],
                                                                        "taskDescription": j['taskDescription'],
                                                                        "startTime": j['startTime'],
                                                                        "endTime": j['endTime'],
                                                                        "userID_id": j['userID_id'],
                                                                        'done': 'In Process'}
                                                                requests.put(
                                                                    url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/",
                                                                    data=data)
                                                    else:
                                                        bot.send_message(message.chat.id, task)
                                                    if task_counter == 0:
                                                        bot.send_message(message.chat.id, "You have no previous tasks",
                                                                         reply_markup=keyboard)
                                bot.send_message(message.chat.id,
                                                 "Please, accept or decline tasks if you haven't done "
                                                 "it yet ☝", reply_markup=keyboard)
                            else:
                                bot.send_message(message.chat.id,
                                                 "Wrong command. Use keyboard below to see your tasks!")
                        bot.register_next_step_handler(func, task_functions)
                        break
                    elif i['username'] == username and i['password'] != message.text:
                        bot.send_message(message.chat.id, "Wrong password. Try logging in again",
                                         reply_markup=back_to_login)

            bot.register_next_step_handler(password, password_check)
        else:
            bot.send_message(message.chat.id, "User not found. Try again", reply_markup=reg_buttons)
    except:
        bot.send_message(message.chat.id, "Error")


def reg(message):
    try:
        url = "http://127.0.0.1:8000/main/users/"
        json_list = requests.get(url).json()
        username = message.text
        counter = 0
        for i in json_list:
            if i['username'] == username:
                counter += 1
                break
        if counter >= 1:
            msg = bot.send_message(message.chat.id, "Username already exists. Try another")
            bot.register_next_step_handler(msg, reg)
        else:
            password1 = bot.send_message(message.chat.id, "Username is correct! Now create a password")

            def password_check(message):
                password2 = bot.send_message(message.chat.id, "Repeat the password")

                def password_check2(msg):
                    if message.text == msg.text:
                        bot.send_message(message.chat.id, "User created. You can login now", reply_markup=reg_buttons)
                        requests.post(url, json={"username": f"{username}",
                                                 "password": f"{msg.text}",
                                                 "userTelegramId": message.from_user.id})
                    else:
                        bot.send_message(message.chat.id, "Passwords didn't match. Try registering again",
                                         reply_markup=reg_buttons)

                bot.register_next_step_handler(password2, password_check2)

            bot.register_next_step_handler(password1, password_check)
    except:
        bot.send_message(message.chat.id, "Error")


# @bot.message_handler(content_types=['text'])
# def task_functions(message):
#     url_users = "http://127.0.0.1:8000/main/users/"
#     url_tasks = "http://127.0.0.1:8000/main/tasks/"
#     json_users_list = requests.get(url_users).json()
#     json_tasks_list = requests.get(url_tasks).json()
#     user_tg_id = message.from_user.id
#     accept_decline = telebot.types.InlineKeyboardMarkup()
#     accept_decline.add(telebot.types.InlineKeyboardButton(text="Decline task", callback_data="Task Decline"))
#     accept_decline.add(telebot.types.InlineKeyboardButton(text="Accept task", callback_data="Task Accept"))
#     if message.text == "Show future tasks":
#         task_counter = 0
#         for i in json_users_list:
#             if i['userTelegramId'] == user_tg_id:
#                 user_id = i['id']
#                 for j in json_tasks_list:
#                     if j['userID_id'] == user_id:
#                         if (j['startTime']).replace('T', ' ').replace('Z', '') > str(datetime.now()):
#                             task = f"Task Name: {j['taskName']}\n\n" \
#                                    f"Description: {j['taskDescription']}\n\n" \
#                                    f"Begins: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
#                                    f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
#                                    f"Status: {j['done']}"
#                             task_counter += 1
#                             if j['done'] != "In Process":
#                                 bot.send_message(message.chat.id, task, reply_markup=accept_decline)
#
#                                 @bot.callback_query_handler(func=lambda call: call.data.startswith('Task'))
#                                 def task_status(call):
#                                     if call.data == "Task Decline":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'],
#                                                 'done': 'Declined'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                                     elif call.data == "Task Accept":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'], 'done': 'In Process'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                             else:
#                                 bot.send_message(message.chat.id, task)
#                             if task_counter == 0:
#                                 bot.send_message(message.chat.id, "You have no future tasks", reply_markup=keyboard)
#                             bot.send_message(message.chat.id, "Please, accept or decline the task if you haven't done "
#                                                               "it yet ☝", reply_markup=keyboard)
#     elif message.text == "Show current tasks":
#         task_counter = 0
#         for i in json_users_list:
#             if i['userTelegramId'] == user_tg_id:
#                 user_id = i['id']
#                 for j in json_tasks_list:
#                     if j['userID_id'] == user_id:
#                         if (j['startTime']).replace('T', ' ').replace('Z', '') < str(datetime.now()) \
#                                 < (j['endTime']).replace('T', ' ').replace('Z', ''):
#                             task = f"Task Name: {j['taskName']}\n\n" \
#                                    f"Description: {j['taskDescription']}\n\n" \
#                                    f"Began: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
#                                    f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
#                                    f"Status: {j['done']}"
#                             task_counter += 1
#                             if j['done'] != "In Process":
#                                 bot.send_message(message.chat.id, task, reply_markup=accept_decline)
#
#                                 @bot.callback_query_handler(func=lambda call: call.data.startswith('Task'))
#                                 def task_status(call):
#                                     if call.data == "Task Decline":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'],
#                                                 'done': 'Declined'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                                     elif call.data == "Task Accept":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'], 'done': 'In Process'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                             else:
#                                 bot.send_message(message.chat.id, task)
#                             if task_counter == 0:
#                                 bot.send_message(message.chat.id, "You have no current tasks", reply_markup=keyboard)
#                             else:
#                                 bot.send_message(message.chat.id, "Please, accept or decline the task if you haven't done "
#                                                                   "it yet ☝", reply_markup=keyboard)
#     elif message.text == "Show previous tasks":
#         task_counter = 0
#         for i in json_users_list:
#             if i['userTelegramId'] == user_tg_id:
#                 user_id = i['id']
#                 for j in json_tasks_list:
#                     if j['userID_id'] == user_id:
#                         if str(datetime.now()) > (j['endTime']).replace('T', ' ').replace('Z', ''):
#                             task = f"Task Name: {j['taskName']}\n\n" \
#                                    f"Description: {j['taskDescription']}\n\n" \
#                                    f"Began: {(j['startTime']).replace('T', ' ').replace('Z', '')}\n" \
#                                    f"Deadline: {(j['endTime']).replace('T', ' ').replace('Z', '')}\n\n" \
#                                    f"Status: {j['done']}"
#                             task_counter += 1
#                             if j['done'] != "In Process":
#                                 bot.send_message(message.chat.id, task, reply_markup=accept_decline)
#
#                                 @bot.callback_query_handler(func=lambda call: call.data.startswith('Task'))
#                                 def task_status(call):
#                                     if call.data == "Task Decline":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'],
#                                                 'done': 'Declined'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                                     elif call.data == "Task Accept":
#                                         data = {'taskName': j['taskName'],
#                                                 "taskDescription": j['taskDescription'],
#                                                 "startTime": j['startTime'],
#                                                 "endTime": j['endTime'],
#                                                 "userID_id": j['userID_id'], 'done': 'In Process'}
#                                         requests.put(url=f"http://127.0.0.1:8000/main/tasks/{j['id']}/", data=data)
#                             else:
#                                 bot.send_message(message.chat.id, task)
#                             if task_counter == 0:
#                                 bot.send_message(message.chat.id, "You have no previous tasks", reply_markup=keyboard)
#                             bot.send_message(message.chat.id, "Please, accept or decline the task if you haven't done "
#                                                               "it yet ☝", reply_markup=keyboard)
#     else:
#         bot.send_message(message.chat.id, "Wrong command. Use keyboard below to see your tasks!")


bot.polling(none_stop=True, interval=0)
