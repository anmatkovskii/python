from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
import pymysql


def main_page(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="tech_shop",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected")
        try:
            with connection.cursor() as cursor:
                data_base = "select * from tech_shop.shop_list"
                cursor.execute(data_base)
                result = cursor.fetchall()
                return render(template_name='tech_shop/main.html', request=request, context={"results": result})
        finally:
            connection.close()

    except:
        print("Error")
