from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView


def main(request):
    return render(request, "city_website/city_main.html")


def news(request):
    return render(request, "city_website/city_news.html")


def city_heads(request):
    return render(request, "city_website/city_heads.html")


def facts(request):
    return render(request, "city_website/city_facts.html")


def contacts(request):
    return render(request, "city_website/city_contacts.html")


def history_main(request):
    return render(request, "city_website/city_history.html")

def history_people(request):
    return render(request, "city_website/city_history_people.html")

def history_photos(request):
    return render(request, "city_website/city_history_photo.html")


