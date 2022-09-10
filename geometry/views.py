from math import pi
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def rectangle_area(request, width: int, height: int):
    area = width * height
    description = f'Площадь прямоугольника со стороной {width} и высотой {height} равна {area}'
    return render(request, 'geometry/rectangle.html')


def square_area(request, width: int):
    area = width ** 2
    description = f'Площадь квадрата со стороной {width} равна {area}'
    return render(request, 'geometry/square.html')


def circle_area(request, radius: int):
    area = pi * radius ** 2
    description = f'Площадь круга радиусом {radius} равна {area}'
    return render(request, 'geometry/circle.html')


def get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('rectangle_area', args=(width, height, ))
    return HttpResponseRedirect(redirect_url)


def get_square_area(request, width: int):
    redirect_url = reverse('square_area', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request, radius: int):
    redirect_url = reverse('circle_area', args=(radius,))
    return HttpResponseRedirect(redirect_url)
