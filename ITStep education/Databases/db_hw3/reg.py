from easygui import *


def login(login, password, connection):
    with connection.cursor() as cursor:
        data = f"select * from users where nickname = '{login.lower()}'"
        cursor.execute(data)
        result = cursor.fetchone()
        if result is not None:
            if result['nickname'].lower() == login.lower():
                if result['password'] == password:
                    return msgbox("Login successful")
                else:
                    return msgbox("Wrong password")
        else:
            return msgbox("No user registered with this nickname")


def register(login, password, name, connection):
    registration = f"""insert into `users`(nickname, password, full_name) values ('{login}','{password}','{name}')"""
    with connection.cursor() as cursor:
        cursor.execute(registration)
        connection.commit()
    return msgbox("Registration successful")