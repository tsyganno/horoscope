from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

dict_day = {
    'monday': 'Пн - стирать',
    'tuesday': 'Вт - учиться',
    'wednesday': 'Ср - гладить',
    'thursday': 'Чт - футбол',
    'friday': 'Пт - кино',
    'saturday': 'Сб - вино',
    'sunday': 'Вс - лежать',
}


def index(request):
    return render(request, 'week_days/greeting.html')


def get_info_about_week_day_by_number(request, week_day: int):
    days = list(dict_day)
    if 0 < week_day < 8:
        day = days[week_day - 1]
        redirect_url = reverse('week_day', args=(day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponse(f'Неверный номер дня - {week_day}')


def get_info_about_week_day(request, week_day: str):
    return HttpResponse(dict_day.get(week_day, f'Не найден день недели {week_day}'))
