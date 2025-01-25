from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from math import pi


def get_rectangle(request, width:int, height:int):
    '''Площадь прямоугольника'''
    area = width * height
    return HttpResponseNotFound(f'Площадь прямоугольника размером {width}х{height} равна {area}')


def get_square(request, width:int):
    '''Площадь квадрата'''
    area = width * width
    return HttpResponseNotFound(f'Площадь квадрата размером {width}х{width} равна {area}')


def get_circle(request, radius:int):
    '''Площадь круга'''
    area = round(pi * radius**2, 3)
    return HttpResponseNotFound(f'Площадь круга радиусом {radius} равна {area}')
