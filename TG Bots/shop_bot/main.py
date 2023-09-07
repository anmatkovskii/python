import json
import telebot
from telebot import types

config = {
    'name': 'ITStep Shop Bot',
    'token': '5857740164:AAFy2hxpceGpVz92EnCqhwPUraHPgXznxgc'
}

bot = telebot.TeleBot(config["token"])

keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Your wallet")
button2 = types.KeyboardButton("Shop")
button3 = types.KeyboardButton("Support")
keyboard1.add(button1, button2, button3)

keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Replenish the balance")
button2 = types.KeyboardButton("Shop")
button3 = types.KeyboardButton("Support")
keyboard2.add(button1)
keyboard2.add(button2, button3)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Welcome to the shop bot!", reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def get_text(message):

    if message.text == "Your wallet":
        wallet(message)

    elif message.text == "Shop":
        shop(message)

    elif message.text == "Support":
        support(message)


def support(message):
    bot.send_message(message.chat.id, "For any support write onto this account @matkovskyi11", reply_markup=keyboard1)

def wallet(message):
    id_list = get_wallets_list()
    user_id = message.from_user.id

    if str(user_id) not in id_list:
        with open("wallet.json", "r") as file:
            data = json.load(file)
        data[str(user_id)] = {"Ballance": "0"}
        with open("wallet.json", "w") as file:
            json.dump(data, file, indent=2)
    with open("wallet.json", "r") as file:
        data = json.load(file)
        next_step = bot.send_message(message.chat.id, f"Your current ballance: {data[str(user_id)]['Ballance']}",
                                     reply_markup=keyboard2)
        user_ballance = data[str(user_id)]['Ballance']

        def replenish(message):
            if message.text == "Replenish the balance":
                bot.send_message(message.chat.id, f"To replenish the balance follow the link: "
                                                  f"https://www.portmone.com.ua/?gclid=CjwKCAiA76-dBhByEiwAA0_s9XZ8toxvZkrmIvsVyOUkmaoXuSVzGhk4pfAcS47wCByJagHSpFoE9BoCtgEQAvD_BwE")
                amount = bot.send_message(message.chat.id, f"Enter the amount of money to replenish")

                def repl_amount(message):
                    if type(message.text) == float:
                        with open("wallet.json", 'r') as file:
                            data = json.load(file)
                            data[str(user_id)] = {
                                "Ballance": float(message.text) + float(data[str(user_id)]['Ballance'])}
                        with open("wallet.json", "w") as file:
                            json.dump(data, file, indent=2)
                        bot.send_message(message.chat.id, f"Your current ballance: {data[str(user_id)]['Ballance']}",
                                         reply_markup=keyboard1)
                    else:
                        bot.send_message(message.chat.id, f"Error", reply_markup=keyboard1)

                bot.register_next_step_handler(amount, repl_amount)
            elif message.text == "Shop":
                shop(message)
            elif message.text == "Support":
                support(message)
        bot.register_next_step_handler(next_step, replenish)

def shop(message):
    with open("shop.txt", "r") as file:
        data = file.read()
        lines = data.splitlines()
        buy_buttons = telebot.types.InlineKeyboardMarkup()
        for i in lines:
            buy_buttons.add(telebot.types.InlineKeyboardButton(text=i, callback_data=f"Buy {i}"))
        buy_buttons.add(
            telebot.types.InlineKeyboardButton(text="Check cart price", callback_data=f"Check cart price"))
    button_check = bot.send_message(message.chat.id, f"Shop items\nJust click to add to cart",
                                    reply_markup=buy_buttons)
    cart = []
    cart_list = []

    @bot.callback_query_handler(func=lambda call: True)
    def shop_action(call):
        if call.data.startswith("Buy"):
            name_and_price = call.data.split(" - ")
            cart_list.append(call.data[4:])
            cart.append(float(name_and_price[1]))
            bot.answer_callback_query(callback_query_id=call.id, text=f"Your added {name_and_price[0][3:]} worth "
                                                                      f"{name_and_price[1]} to your cart")
        elif call.data == "Check cart price":
            bot.answer_callback_query(callback_query_id=call.id, text=f"Your cart is worth {sum(cart)}")

    end_shopping = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Clear cart")
    button2 = types.KeyboardButton("End shopping")
    button3 = types.KeyboardButton("Show cart")
    end_shopping.add(button1, button2, button3)
    cart_choice = bot.send_message(message.chat.id, f"When you end buying, click the button below",
                                   reply_markup=end_shopping)

    def cart_funcs(message):
        if message.text == "Clear cart":
            cart.clear()
            cart_list.clear()
            bot.send_message(message.chat.id, f"Cart cleared!", reply_markup=keyboard1)

        elif message.text == ("End shopping"):
            user_id = message.from_user.id
            with open("wallet.json", "r") as file:
                data = json.load(file)
                user_ballance = data[str(user_id)]['Ballance']
                confirm_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("Yes")
                button2 = types.KeyboardButton("No")
                confirm_keyboard.add(button1, button2)
                if float(user_ballance) >= sum(cart):
                    confirmation = bot.send_message(message.chat.id, f"Your current ballance: "
                                                                     f"{data[str(user_id)]['Ballance']},\n"
                                                                     f"Your cart is worth {sum(cart)}\n"
                                                                     f"After buying your ballance will be "
                                                                     f"{float(data[str(user_id)]['Ballance']) - (sum(cart))}\n "
                                                                     f"Proceed?", reply_markup=confirm_keyboard)

                    def end_shopping(message):
                        if message.text == "Yes":
                            with open("wallet.json", 'r') as file:
                                data = json.load(file)
                                new_ballance = float(data[str(user_id)]['Ballance']) - (sum(cart))
                                data[str(user_id)] = {"Ballance": float(new_ballance)}
                            with open("wallet.json", "w") as file:
                                json.dump(data, file, indent=2)
                            with open("wallet.json", 'r') as file:
                                data = json.load(file)
                                bot.send_message(message.chat.id,
                                                 f"Shopping done!\n"
                                                 f"Your current ballance: {data[str(user_id)]['Ballance']}",
                                                 reply_markup=keyboard1)
                            cart.clear()
                            cart_list.clear()
                        else:
                            bot.send_message(message.chat.id, "Cancelled!", reply_markup=buy_buttons)

                    bot.register_next_step_handler(confirmation, end_shopping)
                elif float(user_ballance) < sum(cart):
                    bot.send_message(message.chat.id, "Not enough money! Clear your cart and buy something again",
                                     reply_markup=buy_buttons)
        elif message.text == "Show cart":
            cart_str = ""
            for i in cart_list:
                cart_str = cart_str + str(i) + "\n"
            bot.send_message(message.chat.id, f"{cart_str}")

    bot.register_next_step_handler(cart_choice, cart_funcs)


def get_wallets_list():
    with open("wallet.json", "r") as file:
        data = json.load(file)
        id_list = data.keys()
        return id_list


bot.polling(none_stop=True, interval=0)
