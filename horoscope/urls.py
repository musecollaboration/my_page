from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type/', views.get_info_type),
    path('type/<element>/', views.get_info_type_element, name='get_info_type_element'),
    path('<int:sign_zodiac>/', views.get_info_about_sing_zodiac_num, name='horoscope-num'),
    path('<str:sign_zodiac>/', views.get_info_about_sing_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>', views.get_zodiac_date),
]
