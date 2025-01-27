from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('sample1', views.sample1),
    path('sample2', views.get_guinness_world_records),

]
