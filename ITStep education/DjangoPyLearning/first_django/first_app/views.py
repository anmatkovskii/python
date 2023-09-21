from django.shortcuts import render
from django.http import HttpResponse
import pymysql


def add(request, product_name, price):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="cart",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                query = f"insert into `product`(name, price) values ('{product_name}', '{price}')"
                cursor.execute(query)
                connection.commit()

        finally:
            connection.close()

    except:
        return HttpResponse("Error")
    return HttpResponse(f'Successfully added {product_name} to your database!')


def show_info(request, product_name):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="cart",
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                query = f"select * from `product` where name = '{product_name}'"
                cursor.execute(query)
                result = cursor.fetchall()
                end_str = "<br>".join([f'Name: {i.get("name")}, Price: {i.get("price")}' for i in result])

        finally:
            connection.close()

    except:
        return HttpResponse("Error")
    return HttpResponse(f'Your product: {end_str}')


def phone_valid(request, phone):
    return HttpResponse(f'Your phone number is correct: {phone}')


def gmail_valid(request, gmail):
    return HttpResponse(f'Your phone number is correct: {gmail}')