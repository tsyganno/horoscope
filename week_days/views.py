from django.shortcuts import render
from django.http import HttpResponse


def get_info_about_week_day(request, week_day):
    dict_day = {
        'monday': 'Пн - стирать',
        'tuesday': 'Вт - учиться',
        'wednesday': 'Ср - гладить',
        'thursday': 'Чт - футбол',
        'friday': 'Пт - кино',
        'saturday': 'Сб - вино',
        'sunday': 'Вс - лежать',
    }
    return HttpResponse(dict_day.get(week_day, f'Не найден день недели {week_day}'))
