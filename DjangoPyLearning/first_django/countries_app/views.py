from django.shortcuts import render


def facts(request):
    return render(request, "country_website/facts.html")


def main(request):
    return render(request, "country_website/main.html")


def cities(request):
    return render(request, "country_website/cities.html")


def history(request):
    return render(request, "country_website/history.html")


def city(request, city_name):
    if city_name.lower() in ["paris", "marseille"]:
        return render(request, f"country_website/city_{str(city_name.lower())}.html")
    else:
        return render(request, "country_website/cities.html")


def city_year(request, city_name, year):
    try:
        if city_name.lower() in ["paris", "marseille"]:
            return render(request, f"country_website/city_{city_name.lower()}_{year}.html")
        else:
            return render(request, "country_website/cities.html")
    except:
        context = {
            'error': "TemplateDoesNotExist"
        }
        return render(request, "country_website/cities.html", context=context)

def history_year(request, year):
    try:
        return render(request, f"country_website/history_{year}.html")

    except:
        context = {
            'error': "TemplateDoesNotExist"
        }
        return render(request, "country_website/history.html", context=context)