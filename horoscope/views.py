from django.shortcuts import render
from django.http import HttpResponse


def leo(request):
    return HttpResponse('leo')

def aries(request):
    return HttpResponse('aries')
