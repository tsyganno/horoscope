from django.contrib import admin
from django.urls import path

from horoscope.views import get_horoscope_by_sign, get_horoscope_by_sign_by_number

urlpatterns = [
    path('<int:sign_of_zodiac>/', get_horoscope_by_sign_by_number),
    path('<str:sign_of_zodiac>/', get_horoscope_by_sign),
]
