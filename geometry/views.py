from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from math import pi


def rectangle(request, width: int, height: int):
    '''Площадь прямоугольника'''
    area = width * height
    context = {'width': width, 'height': height, 'area': area}
    return render(request, 'geometry/rectangle.html', context=context)


def get_rectangle(request, width: int, height: int):
    '''Перенаправление на rectangle'''
    redirec_url = reverse('rectangle', args=[width, height])
    return HttpResponseRedirect(redirec_url)


def square(request, width: int):
    '''Площадь квадрата'''
    area = width * width
    context = {'width': width, 'area': area}
    return render(request, 'geometry/square.html', context=context)


def get_square(request, width: int):
    '''Перенаправление на square'''
    redirec_url = reverse('square', args=[width])
    return HttpResponseRedirect(redirec_url)


def circle(request, radius: int):
    '''Площадь круга'''
    area = round(pi * radius**2, 3)
    context = {'radius': radius, 'area': area}
    return render(request, 'geometry/circle.html', context=context)


def get_circle(request, radius: int):
    '''Перенапрвление на circle'''
    redirec_url = reverse('circle', args=[radius])
    return HttpResponseRedirect(redirec_url)
