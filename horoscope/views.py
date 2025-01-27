from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime as dt


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

elements_zodiac = {
    "fire": ["aries", "leo", "sagittarius"],
    "water": ["cancer", "scorpio", "pisces"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"]
}

zodiac_by_date = {
    "capricorn": ((1, 1), (1, 19)),
    "aquarius": ((1, 20), (2, 18)),
    "pisces": ((2, 19), (3, 20)),
    "aries": ((3, 21), (4, 19)),
    "taurus": ((4, 20), (5, 20)),
    "gemini": ((5, 21), (6, 20)),
    "cancer": ((6, 21), (7, 22)),
    "leo": ((7, 23), (8, 22)),
    "virgo": ((8, 23), (9, 22)),
    "libra": ((9, 23), (10, 22)),
    "scorpio": ((10, 23), (11, 21)),
    "sagittarius": ((11, 22), (12, 21)),
    "capricorn_end": ((12, 22), (12, 31))
}


def index(request):
    'Главное меню'
    li_elemens = ''
    for sing in dict_zodiac:
        redirect_path = reverse('horoscope-name', args=[sing])
        li_elemens += f"<li><a href='{redirect_path}'>{sing.title()}</a></li>"
    response = f'''
    <ul>
        {li_elemens}
    </ul>
    '''
    return HttpResponse(response)


def get_info_type(request):
    '''Стихии'''
    li_elemens = ''
    for element in elements_zodiac:
        redirect_path = reverse('get_info_type_elemens', args=[element])
        li_elemens += f"<li><a href='{redirect_path}'>{element.title()}</a></li>"
    response = f'''
    <ul>
        {li_elemens}
    </ul>
    '''
    return HttpResponse(response)


def get_info_type_elemens(request, element):
    '''Знаки зодиака входящии в стихии'''
    if element not in elements_zodiac:
        return HttpResponseNotFound(f'Такой стихии нет - {element}')
    li_elemens = ''
    for element in elements_zodiac[element]:
        redirect_path = reverse('horoscope-name', args=[element])
        li_elemens += f"<li><a href='{redirect_path}'>{element.title()}</li>"
    response = f'''
    <ul>
        {li_elemens}
    </ul>
    '''
    return HttpResponse(response)


def get_info_about_sing_zodiac(request, sign_zodiac: str):
    '''Информация о знаках зодиака'''
    return render(request, 'horoscope/info_zodiac.html')


def get_info_about_sing_zodiac_num(request, sign_zodiac: int):
    '''Пернаправление на get_info_about_sing_zodiac'''
    lst_zodiac = list(dict_zodiac)
    if sign_zodiac <= len(lst_zodiac):
        name_zodiac = lst_zodiac[sign_zodiac - 1]
        redirect_url = reverse('horoscope-name', args=[name_zodiac])
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Такого номера зодиака нет - {sign_zodiac}')


def get_zodiac_date(request, month: int, day: int):
    '''Узнать знак зодиака по месячу и дате'''
    try:
        for sign in zodiac_by_date:
            data = zodiac_by_date[sign]
            if dt(2000, data[0][0], data[0][1]) <= dt(2000, month, day) <= dt(2000, data[1][0], data[1][1]):
                return HttpResponse(dict_zodiac[sign])
    except:
        return HttpResponseNotFound(f'Вы ошиблись в месяце: {month} или в дне: {day}')
