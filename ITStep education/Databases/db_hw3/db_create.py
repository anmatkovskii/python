import pymysql

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
        with connection.cursor() as cursor:
            create_table = "create table if not exists `users` (id int auto_increment, " \
                           "nickname varchar(30) unique, " \
                           "password varchar(30), " \
                           "full_name varchar(30)," \
                           "primary key (id))"
            create_table2 = "create table if not exists `cart` (cartID int auto_increment, " \
                            "nameBuyer varchar(30), " \
                            "itemName varchar(30), " \
                            "itemPrice int, " \
                            "primary key (cartID)," \
                            "foreign key (nameBuyer) references users (nickname))"
            cursor.execute(create_table)
            cursor.execute(create_table2)

    finally:
        connection.close()

except:
    print("Error")
