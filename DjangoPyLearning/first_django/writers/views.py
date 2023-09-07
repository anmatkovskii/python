from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from operator import itemgetter

context_writers = [
        {'name': 'Andjei Sapkowski',
         'born': '21 червня 1948 (74 роки) Лодзь, Польща',
         'genre': 'фентезі',
         'book': 'Серія книг "Witcher"'},
        {'name': 'William Shakespear',
         'born': '23 квітня 1564р.; Помер: 23 квітня(3 травня) 1616р.',
         'genre': 'драма',
         'book': '"Romeo and Juliet"'}
    ]

context_books = [
        {'book': 'Witcher: The Last Wish',
         'edit': '1993',
         'genre': 'фентезі',
         'author': 'Andjei Sapkowski'},
        {'book': 'Romeo and Juliet',
         'edit': '1597',
         'genre': 'трагедія і мелодрама',
         'author': 'William Shakespear'}
        ]


def main_page(request):
    return render(request, "writers/main.html")


def top_books(request):
    context = {'books': context_books}
    return render(template_name="writers/top_books.html", request=request, context=context)


def writers(request):
    context = {'writers': context_writers}
    return render(template_name="writers/writers.html", request=request, context=context)


# Sort list of dicts by field value !!!
def writer_by_name(request, name):
        context = {'writers': [(next((item for item in context_writers if f"{str(name).lower()}" in item["name"].lower()),
                                     None))]}
        if context == {'writers': [None]}:
            context = {'writers': context_writers}
            return render(template_name="writers/writers.html", request=request, context=context)
        else:
            return render(template_name="writers/writers.html", request=request, context=context)


def book_by_number(request, book):
    try:
        context = {'books': [context_books[int(book)]]}
        return render(template_name="writers/top_books.html", request=request, context=context)
    except:
        context = {'books': context_books}
        return render(template_name="writers/top_books.html", request=request, context=context)


def book_by_name_author(request, name, book):
    context = {'books': [(next((item for item in context_books if f"{str(name).lower()}" in item["author"].lower() and
                                f"{str(book).lower()}" in item["book"].lower()), None))]}
    if context == {'books': [None]}:
        context = {
            'writers': [(next((item for item in context_writers if f"{str(name).lower()}" in item["name"].lower()),
                              None))]}
        return render(template_name="writers/writers.html", request=request, context=context)
    else:
        return render(template_name="writers/top_books.html", request=request, context=context)


def book_by_year(request, name, year):
    context = {'books': [(next((item for item in context_books if f"{str(name).lower()}" in item["author"].lower() and
                                f"{int(year)}" in item["edit"]), None))]}
    print(context)
    if context == {'books': [None]}:
        context = {
            'writers': [(next((item for item in context_writers if f"{str(name).lower()}" in item["name"].lower()),
                              None))]}
        return render(template_name="writers/writers.html", request=request, context=context)
    else:
        return render(template_name="writers/top_books.html", request=request, context=context)