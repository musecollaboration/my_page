from django.urls import path
from . import views


urlpatterns = [
    path('<int:day>/', views.get_info_day_week_num),
    path('<str:day>/', views.get_info_day_week, name='get_info_day_week'),

]
