from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiac>/', views.get_info_about_sing_zodiac_int),
    path('<str:sign_zodiac>/', views.get_info_about_sing_zodiac),

]
