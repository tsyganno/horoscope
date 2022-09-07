from django.contrib import admin
from django.urls import path

from horoscope.views import aries, taurus

urlpatterns = [
    path('horoscope/aries/', aries),
    path('horoscope/taurus/', taurus),
]
