from easygui import *
import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Andrik89@",
        database="sales",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connected")
    try:
        with connection.cursor() as cursor:
            create_table = "create table if not exists `sales` (salesID int auto_increment, " \
                           "nameSalesman varchar(30), " \
                           "nameCustomer varchar(30), " \
                           "nameProduct varchar(30), " \
                           "final_price int, " \
                           "primary key (salesID)," \
                           "foreign key (nameSalesman) references salesmen (name)," \
                           "foreign key (nameCustomer) references customers (name));"
            cursor.execute(create_table)
            create_table2 = "create table if not exists `salesmen` (salesmanID int auto_increment, " \
                            "name varchar(30) unique, " \
                            "phone varchar(30), " \
                            "primary key (salesmanID));"
            cursor.execute(create_table2)
            create_table3 = "create table if not exists `customers` (customerID int auto_increment, " \
                            "name varchar(30) unique, " \
                            "phone varchar(30), " \
                            "primary key (customerID));"
            cursor.execute(create_table3)
        # with connection.cursor() as cursor:
        #     insert = "insert into `salesmen` (name, phone) values ('Sasha', '0992046287'), ('Max', '0992619427')"
        #     insert2 = "insert into `customers` (name, phone) values ('Mykola', '0916289287'), ('Bogdan', '0992039661')"
        #     insert3 = "insert into `sales` (nameSalesman, nameCustomer, nameProduct, final_price) values ('Sasha', " \
        #               "'Mykola', 'Iphone', '1000')"
        #     cursor.execute(insert)
        #     cursor.execute(insert2)
        #     cursor.execute(insert3)
        #     connection.commit()

        with connection.cursor() as cursor:
            while True:
                interface = buttonbox("Choose action: ", "Action",
                                      ["SELECT DATA", "INSERT", "DELETE", "UPDATE", "EXIT"])
                if interface == "EXIT":
                    break

                elif interface == "SELECT DATA":
                    select_interface = buttonbox("Choose action: ", "Action", ["Show All sales", "Salesmen data",
                                                                               "Customers data", "EXIT"])
                    if select_interface == "Show All sales":
                        data = f"select * from sales"
                        cursor.execute(data)
                        result = cursor.fetchall()
                        generated_list = []
                        for i in result:
                            generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, Customer:"
                                                  f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                  f" Price: {i.get('final_price')}\n")
                        msgbox("\n".join(generated_list))

                    elif select_interface == "Salesmen data":
                        choice = buttonbox("Who to check: ", "Check", ["One salesman", "For all salesmen"])
                        if choice == "One salesman":
                            salesman = enterbox("Enter salesman's name")
                            salesmen_data = buttonbox("What to show: ", "Show", ["All sales", "Max sale", "Min sale",
                                                                                 "Average sale"])
                        elif choice == "For all salesmen":
                            salesmen_data = buttonbox("What to show: ", "Show", ["Max total sales", "Min total sales"])

                        if salesmen_data == "All sales":
                            data = f"select * from sales where nameSalesman = '{salesman}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, "
                                                      f"Customer: "
                                                      f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                      f" Price: {i.get('final_price')}\n")
                            msgbox("\n".join(generated_list))

                        elif salesmen_data == "Max sale":
                            data = f"SELECT salesID, nameSalesman, nameCustomer, nameProduct, final_price from sales " \
                                   f"where final_price = (select max(final_price) from sales) and " \
                                   f"nameSalesman = '{salesman}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, "
                                                      f"Customer: "
                                                      f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                      f" Price: {i.get('final_price')}\n")
                            msgbox("\n".join(generated_list))

                        elif salesmen_data == "Min sale":
                            data = f"SELECT salesID, nameSalesman, nameCustomer, nameProduct, final_price from sales " \
                                   f"where final_price = (select min(final_price) from sales) and " \
                                   f"nameSalesman = '{salesman}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, "
                                                      f"Customer: "
                                                      f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                      f" Price: {i.get('final_price')}\n")
                            msgbox("\n".join(generated_list))

                        elif salesmen_data == "Average sale":
                            data = f"SELECT nameSalesman, avg(final_price) from sales where nameSalesman = '{salesman}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"Salesman: {i.get('nameSalesman')}, Average price: "
                                                      f"{i.get('avg(final_price)')}\n")
                            msgbox("\n".join(generated_list))

                        elif salesmen_data == "Min total sales":
                            data = f"select nameSalesman, sum(final_price) from sales group by nameSalesman order by " \
                                   f"final_price desc "
                            cursor.execute(data)
                            i = cursor.fetchone()
                            result = f"Salesman: {i.get('nameSalesman')}, Min sales price: " \
                                     f"{i.get('sum(final_price)')}\n"
                            msgbox(result)

                        elif salesmen_data == "Max total sales":
                            data = f"select nameSalesman, sum(final_price) from sales group by nameSalesman order by " \
                                   f"final_price "
                            cursor.execute(data)
                            i = cursor.fetchone()
                            result = f"Salesman: {i.get('nameSalesman')}, Max sales price: " \
                                     f"{i.get('sum(final_price)')}\n"
                            msgbox(result)

                    elif select_interface == "Customers data":
                        customers_data = buttonbox("What to show: ", "Show", ["Max sale", "Min sale",
                                                                              "Max total sales", "Average sale"])

                        if customers_data == "Max sale":
                            customer = enterbox("Enter customer's name")
                            data = f"SELECT salesID, nameSalesman, nameCustomer, nameProduct, final_price from sales " \
                                   f"where final_price = (select max(final_price) from sales) and " \
                                   f"nameCustomer = '{customer}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, "
                                                      f"Customer: "
                                                      f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                      f" Price: {i.get('final_price')}\n")
                            msgbox("\n".join(generated_list))

                        elif customers_data == "Min sale":
                            customer = enterbox("Enter customer's name")
                            data = f"SELECT salesID, nameSalesman, nameCustomer, nameProduct, final_price from sales " \
                                   f"where final_price = (select min(final_price) from sales) and " \
                                   f"nameCustomer = '{customer}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"id:{i.get('salesID')}, Salesman: {i.get('nameSalesman')}, "
                                                      f"Customer: "
                                                      f" {i.get('nameCustomer')}, Product: {i.get('nameProduct')},"
                                                      f" Price: {i.get('final_price')}\n")
                            msgbox("\n".join(generated_list))

                        elif customer_data == "Max total sales":
                            data = f"select nameCustomer, sum(final_price) from sales group by nameSalesman order by " \
                                   f"final_price "
                            cursor.execute(data)
                            i = cursor.fetchone()
                            result = f"Customer: {i.get('nameSalesman')}, Max sales price: " \
                                     f"{i.get('sum(final_price)')}\n"
                            msgbox(result)

                        elif customer_data == "Average sale":
                            data = f"SELECT nameCustomer, avg(final_price) from sales where nameSalesman = '{salesman}'"
                            cursor.execute(data)
                            result = cursor.fetchall()
                            generated_list = []
                            for i in result:
                                generated_list.append(f"Customer: {i.get('nameCustomer')}, Average price: "
                                                      f"{i.get('avg(final_price)')}\n")
                            msgbox("\n".join(generated_list))

                elif interface == "INSERT":
                    table_choice = buttonbox("Choose action: ", "Action",
                                             ["Add new sale", "Add new customer", "Add new salesman"])
                    if table_choice == "Add new sale":
                        data = multenterbox("Enter info to insert:", "Insert", ["Salesman", "Customer",
                                                                                "Product", "Price"])
                        insert = "insert into `sales` (nameSalesman, nameCustomer, nameProduct, final_price) values " \
                                 f"('{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}')"
                        cursor.execute(insert)
                        connection.commit()
                    elif table_choice == "Add new customer":
                        data = multenterbox("Enter info to insert:", "Insert", ["Customer", "Phone"])
                        insert = f"insert into `customers` (name, phone) values ('{data[0]}', '{data[1]}')"
                        cursor.execute(insert)
                        connection.commit()
                    elif table_choice == "Add new salesman":
                        data = multenterbox("Enter info to insert:", "Insert", ["Salesman", "Phone"])
                        insert = f"insert into `salesmen` (name, phone) values ('{data[0]}', '{data[1]}')"
                        cursor.execute(insert)
                        connection.commit()

                elif interface == "DELETE":
                    table_choice = buttonbox("Choose table: ", "Action",
                                             ["Sales", "Salesmen", "Customers"])
                    id_delete = enterbox("Enter what ID to delete")
                    if table_choice == "Sales":
                        delete_data = f"delete from `sales` where salesID={int(id_delete)}"
                        cursor.execute(delete_data)
                        connection.commit()
                    elif table_choice == "Salesmen":
                        delete_data = f"delete from `salesmen` where salesmanID={int(id_delete)}"
                        cursor.execute(delete_data)
                        connection.commit()
                    elif table_choice == "Customers":
                        delete_data = f"delete from `customers` where customerID={int(id_delete)}"
                        cursor.execute(delete_data)
                        connection.commit()

                elif interface == "UPDATE":
                    table_choice = buttonbox("Choose table: ", "Action",
                                             ["Sales", "Salesmen", "Customers"])
                    get_id = enterbox("Enter what ID to update")
                    if table_choice == "Sales":
                        data1 = f"select * from `sales` where salesID in ({get_id})"
                        cursor.execute(data1)
                        result = cursor.fetchone()
                        data = multenterbox("Enter info to update:", "Update",
                                            ["Salesman", "Customer", "Product", "Price"],
                                            [f"{result.get('nameSalesman')}", f"{result.get('nameCustomer')}",
                                             f"{result.get('nameProduct')}", f"{result.get('final_price')}"])
                        update_data = f"update `sales` set nameSalesman = '{data[0]}', nameCustomer = '{data[1]}', " \
                                      f"nameProduct = '{data[2]}', final_price = '{data[3]}' where salesID={get_id}"
                        cursor.execute(update_data)
                        connection.commit()

                    elif table_choice == "Salesmen":
                        data1 = f"select * from `salesmen` where salesmanID in ({get_id})"
                        cursor.execute(data1)
                        result = cursor.fetchone()
                        data = multenterbox("Enter info to update:", "Update",
                                            ["Name", "Phone"],
                                            [f"{result.get('name')}", f"{result.get('phone')}"])
                        update_data = f"update `salesmen` set name = '{data[0]}', phone = '{data[1]}' "
                        cursor.execute(update_data)
                        connection.commit()

                    elif table_choice == "Customers":
                        data1 = f"select * from `customers` where customerID in ({get_id})"
                        cursor.execute(data1)
                        result = cursor.fetchone()
                        data = multenterbox("Enter info to update:", "Update",
                                            ["Name", "Phone"],
                                            [f"{result.get('name')}", f"{result.get('phone')}"])
                        update_data = f"update `customers` set name = '{data[0]}', phone = '{data[1]}' "
                        cursor.execute(update_data)
                        connection.commit()
    finally:
        connection.close()

except:
    print("Error")
