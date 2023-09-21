from easygui import *
import pymysql


try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Andrik89@",
        database="practice1",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    try:
        with connection.cursor() as cursor:
            create_table = "create table if not exists `people` (id int auto_increment, " \
                           "first_name varchar(30), " \
                           "last_name varchar(30), " \
                           "city varchar(30), " \
                           "country varchar(30), " \
                           "birthday varchar(30)," \
                           "primary key (id))"
            cursor.execute(create_table)

        with connection.cursor() as cursor:
            while True:
                interface = buttonbox("Choose action: ", "Action",
                                      ["SELECT DATA", "INSERT", "DELETE", "UPDATE", "EXIT"])
                if interface == "EXIT":
                    break

                elif interface == "SELECT DATA":
                    select_interface = buttonbox("Choose action: ", "Action", ["SELECT BY ID", "SELECT ALL", "EXIT"])
                    if select_interface == "SELECT BY ID":
                        search_range = enterbox("Enter what ID to search. [1]/[1, 2, 3]")
                        data = f"select * from people where id in({search_range})"
                        cursor.execute(data)
                        result = cursor.fetchall()
                        for i in result:
                            msgbox(i, 'SELECT results', 'NEXT')                   # Work on output!
                    elif select_interface == "SELECT ALL":
                        data = f"select * from people"
                        cursor.execute(data)
                        result = cursor.fetchall()
                        for i in result:
                            msgbox(i, 'SELECT results', 'NEXT')                   # Work on output!
                    else:
                        break

                elif interface == "INSERT":
                    data = multenterbox("Enter info to insert:", "Insert", ["First name", "Last name", "City",
                                                                            "Country", "Birthday"])
                    insert = "insert into `people` (first_name, last_name, city, country, birthday) values " \
                             f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}')"
                    cursor.execute(insert)
                    connection.commit()

                elif interface == "DELETE":
                    id_delete = enterbox("Enter what ID to delete")
                    delete_data = f"delete from `people` where id={int(id_delete)}"
                    cursor.execute(delete_data)
                    connection.commit()

                elif interface == "UPDATE":
                    get_id = enterbox("Enter what ID to update")
                    data1 = f"select * from people where id in ({get_id})"
                    cursor.execute(data1)
                    result = cursor.fetchone()
                    data = multenterbox("Enter info to update:", "Insert",
                                        ["First name", "Last name", "City", "Country", "Birthday"],
                                        [result['first_name'], result['last_name'], result['city'], result['country'],
                                         result['birthday']])
                    update_data = f"update `people` set first_name = '{data[0]}', last_name = '{data[1]}', city = " \
                                  f"'{data[2]}', country = '{data[3]}', birthday = '{data[4]}' where id={get_id}"
                    cursor.execute(update_data)
                    connection.commit()
    finally:
        connection.close()

except:
    print("Error")
