from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}

zodiac_element = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

zodiac_dates = {
    1:  {'capricorn': (1, 20),   'aquarius': (21, 31)},
    2:  {'aquarius': (1, 19),    'pisces': (20, 29)},
    3:  {'pisces': (1, 20),      'aries': (21, 31)},
    4:  {'aries': (1, 20),       'taurus': (21, 30)},
    5:  {'taurus': (1, 21),      'gemini': (22, 31)},
    6:  {'gemini':  (1, 21),     'cancer': (22, 30)},
    7:  {'cancer':  (1, 22),     'leo': (23, 31)},
    8:  {'leo': (1, 21),         'virgo': (22, 31)},
    9:  {'virgo': (1, 22),       'libra': (23, 30)},
    10: {'libra': (1, 23),       'scorpio': (24, 31)},
    11: {'scorpio': (1, 22),     'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
}


def index(request):
    zodiacs = list(signs)
    return render(
        request,
        'horoscope/index.html',
        {
            'zodiacs': zodiacs
        }
    )


def get_horoscope_by_sign_by_number(request, sign_of_zodiac: int):
    zodiacs = list(signs)
    if sign_of_zodiac > (len(zodiacs)) or sign_of_zodiac <= 0:
        return HttpResponse("Неизвестный знак зодиака")
    name_zodiac = zodiacs[sign_of_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)


def get_horoscope_by_sign(request, sign_of_zodiac: str):
    sign = signs.get(sign_of_zodiac)
    return render(
        request,
        'horoscope/info_zodiac.html',
        {
            'description': sign,
            'sign': sign_of_zodiac,
            'zodiacs': signs
        }
    )


def get_horoscope_type(request):
    zodiacs = list(zodiac_element)
    response = '<br>'.join(zodiacs)
    return HttpResponse(response)


def get_horoscope_type_element(request, element: str):
    for key in zodiac_element.keys():
        if key == element:
            response = '<br>'.join(zodiac_element[key])
            return HttpResponse(response)


def get_info_about_zodiac_by_day(request, month: int, day: int):
    try:
        for sign, dates in zodiac_dates[month].items():
            if dates[0] <= day <= dates[1]:
                redirect_url = reverse('horoscope_name', args=(sign, ))
                return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound(f"Что Вы имеете ввиду под месяцем - {month} и днем - {day}?")