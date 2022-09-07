from django.contrib import admin
from django.urls import path

from horoscope.views import get_horoscope_by_sign

urlpatterns = [
    path('<str:sign_of_zodiac>/', get_horoscope_by_sign),
]
