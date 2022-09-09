from django.contrib import admin
from django.urls import path

from week_days.views import get_info_about_week_day, get_info_about_week_day_by_number

urlpatterns = [
    path('<int:week_day>/', get_info_about_week_day_by_number),
    path('<str:week_day>/', get_info_about_week_day, name='week_day'),
]
