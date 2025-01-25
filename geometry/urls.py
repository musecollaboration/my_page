from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle),
    path('square/<int:width>/', views.get_square),
    path('circle/<int:radius>/', views.get_circle),

]
