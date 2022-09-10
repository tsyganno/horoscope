from django.contrib import admin
from django.urls import path

from horoscope.views import index, get_horoscope_by_sign, get_horoscope_by_sign_by_number, get_horoscope_type, \
    get_horoscope_type_element, get_info_about_zodiac_by_day

urlpatterns = [
    path('', index, name='index'),
    path('type/', get_horoscope_type),
    path('type/<str:element>/', get_horoscope_type_element),
    path('<int:sign_of_zodiac>/', get_horoscope_by_sign_by_number),
    path('<str:sign_of_zodiac>/', get_horoscope_by_sign, name='horoscope_name'),
    path('<int:month>/<int:day>/', get_info_about_zodiac_by_day),
]
