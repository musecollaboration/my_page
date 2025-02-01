from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('sample1', views.sample1),
    path('sample2', views.get_guinness_world_records),
    path('people', views.get_info_people),
    path('people_detail', views.get_info_people_detail),
    path('beautiful_table', views.get_table),
    path('test_temp', views.get_test_temp),

]
