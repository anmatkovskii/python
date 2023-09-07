from easygui import *
import pymysql
from reg import *
from cart_func import *

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="yourpass",
        database="koshyk",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    try:
        while True:
            request = buttonbox("Choose action: ", "Action", ["LOGIN", "REGISTER", "EXIT"])
            if request == "EXIT":
                break
            elif request == "REGISTER":
                register_form = multpasswordbox("Login", "Login", ["Login", "Name", "Password"])
                register(register_form[0], register_form[2], register_form[1], connection)
            elif request == "LOGIN":
                password_enter = multpasswordbox("Login", "Login", ["Login", "Password"])
                login(password_enter[0], password_enter[1], connection)
                while True:
                    request = buttonbox("My shopping cart", "My shopping cart", ["Add to cart", "Remove from cart",
                                                                                 "Replace item in cart", "Clear cart",
                                                                                 "Search cart item by name",
                                                                                 "Show your cart",
                                                                                 "EXIT"])
                    if request == "EXIT":
                        break
                    elif request == "Add to cart":
                        add_to_cart(password_enter[0], connection)
                    elif request == "Remove from cart":
                        remove_from_cart(password_enter[0], connection)
                    elif request == "Replace item in cart":
                        replace_item(password_enter[0], connection)
                    elif request == "Clear cart":
                        clear_cart(password_enter[0], connection)
                    elif request == "Search cart item by name":
                        search_by_name(password_enter[0], connection)
                    elif request == "Show your cart":
                        show_all(password_enter[0], connection)
    finally:
        connection.close()

except:
    print("Error")
