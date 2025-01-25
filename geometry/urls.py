from django.urls import path
from . import views

urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle),
    path('get_square_area/<int:width>', views.get_square),
    path('get_circle_area/<int:radius>', views.get_circle),
    path('rectangle/<int:width>/<int:height>/', views.rectangle),
    path('square/<int:width>/', views.square),
    path('circle/<int:radius>/', views.circle),

]
