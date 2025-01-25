from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from math import pi


def rectangle(request, width: int, height: int):
    '''Площадь прямоугольника'''
    area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {area}')


def get_rectangle(request, width: int, height: int):
    '''Перенаправление на rectangle'''
    return HttpResponseRedirect(f"/calculate_geometry/rectangle/{width}/{height}/")


def square(request, width: int):
    '''Площадь квадрата'''
    area = width * width
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {area}')


def get_square(request, width: int):
    '''Перенаправление на square'''
    return HttpResponseRedirect(f"/calculate_geometry/square/{width}/")


def circle(request, radius: int):
    '''Площадь круга'''
    area = round(pi * radius**2, 3)
    return HttpResponse(f'Площадь круга радиусом {radius} равна {area}/')


def get_circle(request, radius: int):
    '''Перенапрвление на circle'''
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}/')
