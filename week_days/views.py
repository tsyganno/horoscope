from django.shortcuts import render
from django.http import HttpResponse


def monday(request):
    return HttpResponse('Понедельник')


def tuesday(request):
    return HttpResponse('Вторник')
