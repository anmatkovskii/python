from easygui import *


def add_to_cart(login, connection):
    with connection.cursor() as cursor:
        data = multenterbox("Enter item to cart", "Input", ["Item Name", "Price"])
        insert = "insert into `cart` (nameBuyer, itemName, itemPrice) values " \
                 f"('{login}', '{data[0].strip()}', '{data[1].strip()}')"
        cursor.execute(insert)
        connection.commit()
    return msgbox("Added!")


def remove_from_cart(login, connection):
    id_delete = enterbox("Enter id of item to remove")
    with connection.cursor() as cursor:
        delete_data = f"delete from `cart` where cartID={int(id_delete)} and nameBuyer='{login}'"
        cursor.execute(delete_data)
        connection.commit()
    return msgbox("Done!")


def replace_item(login, connection):
    get_id = enterbox("Enter what ID to update")
    with connection.cursor() as cursor:
        data1 = f"select * from `cart` where cartID={int(get_id)} and nameBuyer='{login}'"
        cursor.execute(data1)
        result = cursor.fetchone()
        data = multenterbox("Enter info to replace:", "Replace",
                            ["Item name", "Price"],
                            [f"{result.get('itemName')}", f"{result.get('itemPrice')}"])
        update_data = f"update `cart` set itemName = '{data[0].strip()}', itemPrice = '{data[1].strip()}' " \
                      f"where cartID={int(get_id)} and nameBuyer='{login}' "
        cursor.execute(update_data)
        connection.commit()
    return msgbox("Done!")


def clear_cart(login, connection):
    ask = buttonbox("Are you sure you want to clear your cart?\nDeleted data can't be restored", "Warn", ["YES", "NO"])
    if ask == "YES":
        with connection.cursor() as cursor:
            delete_data = f"delete from `cart` where nameBuyer='{login}'"
            cursor.execute(delete_data)
            connection.commit()
        return msgbox("Done!")
    else:
        pass


def search_by_name(login, connection):
    get_name = enterbox("Enter name of item to search")
    with connection.cursor() as cursor:
        delete_data = f"select * from `cart` where itemName='{get_name}' and nameBuyer='{login}'"
        cursor.execute(delete_data)
        result = cursor.fetchall()
        generated_list = []
        for i in result:
            generated_list.append(f"id:{i.get('cartID')} | "
                                  f"Item name: {i.get('itemName')}, Price: {i.get('itemPrice')}")
    return msgbox("\n".join(generated_list))


def show_all(login, connection):
    with connection.cursor() as cursor:
        delete_data = f"select * from `cart` where nameBuyer='{login}'"
        cursor.execute(delete_data)
        result = cursor.fetchall()
        generated_list = []
        for i in result:
            generated_list.append(f"id:{i.get('cartID')}, | "
                                  f"Item name: {i.get('itemName')}, Price: {i.get('itemPrice')}")
    return msgbox("\n".join(generated_list))