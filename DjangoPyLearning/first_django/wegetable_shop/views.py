from django.shortcuts import render
from wegetable_shop.models import ProductGrocery


def main_page(request):
    context = ProductGrocery.objects.all()
    return render(template_name='wegetable_shop/main.html', request=request, context={"product_list": context})


def get_fruits(request):
    context = ProductGrocery.objects.filter(type="FRUIT").values()
    return render(template_name='wegetable_shop/main.html', request=request, context={"product_list": context})


def get_vegetables(request):
    context = ProductGrocery.objects.filter(type="VEGETABLE").values()
    return render(template_name='wegetable_shop/main.html', request=request, context={"product_list": context})