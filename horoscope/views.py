from django.shortcuts import render
from django.http import HttpResponse


def aries(request):
    return HttpResponse('Знак зодиака Овен')


def taurus(request):
    return HttpResponse('Знак зодиака Телец')

