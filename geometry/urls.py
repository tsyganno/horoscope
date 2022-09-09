from django.contrib import admin
from django.urls import path

from geometry.views import rectangle_area, square_area, circle_area, get_rectangle_area, get_square_area, get_circle_area

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', rectangle_area, name='rectangle_area'),
    path('square/<int:width>/', square_area, name='square_area'),
    path('circle/<int:radius>/', circle_area, name='circle_area'),
    path('get_rectangle_area/<int:width>/<int:height>', get_rectangle_area),
    path('get_square_area/<int:width>', get_square_area),
    path('get_circle_area/<int:radius>', get_circle_area),
]
