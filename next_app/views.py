from datetime import datetime

from django.shortcuts import render, HttpResponse
from django.utils.html import escape



class Cow:
    def __init__(self, name):
        self.name = name
# Create your views here.


def hello(request):
    return HttpResponse("Hello world!")


def name(request, data):
    escaped_data = escape(data)
    return HttpResponse(f"Hello, {escaped_data}!")


def hello2(request):
    return render(
        request,
        'next_app/hello.html'
    )


def name2(request, data):
    return render(
        request,
        'name.html',
        context={
            'data': data

        },
    )


def is_it_new_year(request):
    now = datetime.now()

    is_new_year = False

    if now.day == 1 and now.month == 1:
        is_new_year = True

    return render(
        request,
        'is_it_new_year.html',
        context={
            'is_new_year': is_new_year,
        }

    )


def fruits(request):

    fruits_list = [
        'jabłko',
        'banan',
        'winogrona',
        'mandarynki',

    ]


    person = {

        "name": "Jan",
        "surname": "Kowalski",
        "age": 15,
    }

    cow = Cow(name="Mućka")

    return render(
        request,
        'fruits.html',
        context= {
            'fruits': fruits_list,
            'person': person,
            'cow': cow,
        }
    )