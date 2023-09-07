from django.shortcuts import render

def main_page(request):
    return render(request, 'second_app/main.html')