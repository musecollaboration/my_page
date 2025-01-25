from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi


def rectangle(request, width: int, height: int):
    '''Площадь прямоугольника'''
    area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {area}')


def get_rectangle(request, width: int, height: int):
    '''Перенаправление на rectangle'''
    redirec_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(redirec_url)


def square(request, width: int):
    '''Площадь квадрата'''
    area = width * width
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {area}')


def get_square(request, width: int):
    '''Перенаправление на square'''
    redirec_url = reverse('square', args=[width])
    return HttpResponseRedirect(redirec_url)


def circle(request, radius: int):
    '''Площадь круга'''
    area = round(pi * radius**2, 3)
    return HttpResponse(f'Площадь круга радиусом {radius} равна {area}')


def get_circle(request, radius: int):
    '''Перенапрвление на circle'''
    redirec_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(redirec_url)
