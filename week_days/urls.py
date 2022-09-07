from django.contrib import admin
from django.urls import path

from week_days.views import monday, tuesday

urlpatterns = [
    path('todo_week/monday/', monday),
    path('todo_week/tuesday/', tuesday),
]