from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')
register_converter(converters.SplitConverter, 'split')


urlpatterns = [
    path('', views.index),
    path('<split:sign_zodiac>', views.get_split),
    path('<my_date:sign_zodiac>', views.get_my_date_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sing_zodiac, name='horoscope-name'),
    path('type/<element>/', views.get_info_type_elemens, name='get_info_type_elemens'),
    path('<yyyy:sign_zodiac>', views.get_yyyy_converters),
    path('<int:sign_zodiac>/', views.get_info_about_sing_zodiac_num),
    path('<my_float:sign_zodiac>', views.get_my_float_converters),
    path('<int:month>/<int:day>', views.get_zodiac_date),
]
