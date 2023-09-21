from django.shortcuts import render
import pymysql


def main_page_library(request):
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Andrik89@",
            database="library",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected")
        try:
            with connection.cursor() as cursor:
                data = f"select * from library.books"
                cursor.execute(data)
                result = cursor.fetchall()
        finally:
            connection.close()

    except:
        print("Error")

    return render(template_name='library/library_main_page.html', request=request, context={"results": result})
