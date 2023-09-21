from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime
import pymysql
from second_app.models import Product



def dbshow(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="sakila",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected")
        try:
            with connection.cursor() as cursor:
                data_base = "select * from sakila.students"
                cursor.execute(data_base)
                result = cursor.fetchall()
        finally:
            connection.close()  

    except:
        print("Error")
    return render(template_name='second_app/bootstrap.html', request=request, context={"students": result})

def dictsort(request):
    context = {"questions": [{'priority': 100, 'task': 'Составить список дел'},
                             {'priority': 150, 'task': 'Изучать Django'},
                             {'priority': 1, 'task': 'Подумать о смысле жизни'}]}
    return render(template_name='second_app/bootstrap.html', request=request, context=context)


def product(request):
    context = Product.objects.all()
    return render(template_name='second_app/main2.html', request=request, context={"product_list":context})


def main_page(request):
    return render(request, 'second_app/main.html')


def about(request):
    return render(request, 'second_app/about.html')


def contacts(request):
    return render(request, 'second_app/contacts.html')


def news(request):
    return render(request, 'second_app/news.html')


def rulers(request):
    return render(request, 'second_app/rulers.html')
