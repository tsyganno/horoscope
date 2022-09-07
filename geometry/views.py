from math import pi
from django.shortcuts import render
from django.http import HttpResponse


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    description = f'Площадь прямоугольника со стороной {width} и высотой {height} равна {area}'
    return HttpResponse(description)


def get_square_area(request, width: int):
    area = width ** 2
    description = f'Площадь квадрата со стороной {width} равна {area}'
    return HttpResponse(description)


def get_circle_area(request, radius: int):
    area = pi * radius ** 2
    description = f'Площадь круга радиусом {radius} равна {area}'
    return HttpResponse(description)
