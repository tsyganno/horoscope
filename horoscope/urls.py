from django.contrib import admin
from django.urls import path

from horoscope.views import index, get_horoscope_by_sign, get_horoscope_by_sign_by_number, get_horoscope_type, get_horoscope_type_element

urlpatterns = [
    path('', index),
    path('type/', get_horoscope_type),
    path('type/<str:element>/', get_horoscope_type_element),
    path('<int:sign_of_zodiac>/', get_horoscope_by_sign_by_number),
    path('<str:sign_of_zodiac>/', get_horoscope_by_sign, name='horoscope_name'),
]
