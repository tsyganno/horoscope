from django.contrib import admin
from django.urls import path

from week_days.views import get_horoscope_by_sign

urlpatterns = [
    path('<str:sign_of_zodiac>/', get_horoscope_by_sign),
]
