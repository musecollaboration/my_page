from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:sign_zodiac>/', views.get_info_about_sing_zodiac_num),
    path('<str:sign_zodiac>/', views.get_info_about_sing_zodiac, name='horoscope-name'),

]
