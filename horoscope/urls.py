from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.get_info_type),
    path('type/<element>/', views.get_info_type_elemens, name='get_info_type_elemens'),
    path('<int:sign_zodiac>/', views.get_info_about_sing_zodiac_num),
    path('<str:sign_zodiac>/', views.get_info_about_sing_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>', views.get_zodiac_date),

]
