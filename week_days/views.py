from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

dict_day = {
    'monday': 'Пн - стирать',
    'tuesday': 'Вт - учиться',
    'wednesday': 'Ср - гладить',
    'thursday': 'Чт - футбол',
    'friday': 'Пт - кино',
    'saturday': 'Сб - вино',
    'sunday': 'Вс - лежать',
}


def get_info_about_week_day_by_number(request, week_day: int):
    days = list(dict_day)
    if 0 < week_day < 8:
        return HttpResponseRedirect(f'/todo_week/{days[week_day - 1]}')
    else:
        return HttpResponse(f'Неверный номер дня - {week_day}')


def get_info_about_week_day(request, week_day: str):
    return HttpResponse(dict_day.get(week_day, f'Не найден день недели {week_day}'))
