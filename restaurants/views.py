from django.shortcuts import render
from .models import Restaurant

def get_restaurants():
    rest= Restaurant.objects.values()
    print(rest)
    return rest

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    restaurants = get_restaurants()
    context = {
        "restaurants": restaurants,
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(pk=restaurant_id),
    }
    return render(request, 'detail.html', context)
