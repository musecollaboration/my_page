from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

dict_zodiac = {
    'aries': 'Овен - первый знак зодиака. Рожден 21 марта - 20 апреля',
    'taurus': 'Телец - второй знак зодиака. Рожден 21 апреля - 21 мая',
    'gemini': 'Близнецы - третий знак зодиака. Рожден 22 мая - 21 июня',
    'cancer': 'Рак - четвёртый знак зодиака. Рожден 22 июня - 22 июля',
    'leo': 'Лев - пятый знак зодиака. Рожден 23 июля - 21 августа',
    'virgo': 'Дева - шестой знак зодиака. Рожден 22 августа - 23 сентября',
    'libra': 'Весы - седьмой знак зодиака. Рожден 24 сентября - 23 октября',
    'scorpio': 'Скорпион - восьмой знак зодиака. Рожден 24 октября - 22 ноября',
    'sagittarius': 'Стрелец - девятый знак зодиака. Рожден 23 ноября - 21 декабря',
    'capricorn': 'Козерог - десятый знак зодиака. Рожден 22 декабря - 20 января',
    'aquarius': 'Водолей - одиннадцатый знак зодиака. Рожден 21 января - 19 февраля',
    'pisces': 'Рыбы - двенадцатый знак зодиака. Рожден 20 февраля - 20 марта'
}


def get_info_about_sing_zodiac(request, sign_zodiac: str):
    '''Информация о знаках зодиака'''
    if sign_zodiac in dict_zodiac:
        return HttpResponse(dict_zodiac[sign_zodiac])
    return HttpResponseNotFound(f'Такого знака зодиака нет - {sign_zodiac}')


def get_info_about_sing_zodiac_int(request, sign_zodiac: int):
    '''Поиск по номеру знака зодиака'''
    lst_zodiac = list(dict_zodiac)
    if sign_zodiac <= len(lst_zodiac):
        return HttpResponse(dict_zodiac[lst_zodiac[sign_zodiac - 1]])
    return HttpResponseNotFound(f'Такого номера зодиака нет - {sign_zodiac}')
