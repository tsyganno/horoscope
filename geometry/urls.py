from django.contrib import admin
from django.urls import path

from geometry.views import get_rectangle_area, get_square_area, get_circle_area

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', get_rectangle_area),
    path('square/<int:width>/', get_square_area),
    path('circle/<int:radius>/', get_circle_area),
]
