from django.urls import path
from . import views


urlpatterns = [
    path('<day>/', views.get_info_day_week),
]
