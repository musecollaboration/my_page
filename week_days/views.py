from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


dict_days_of_week = {
    "monday": "День недели понедельник, будний день начало недели",
    "tuesday": "День недели вторник, будний день второй день недели",
    "wednesday": "День недели среда, будний день середина недели",
    "thursday": "День недели четверг, будний день преддверие выходных",
    "friday": "День недели пятница, будний день конец рабочей недели",
    "saturday": "День недели суббота, выходной день, время отдыха",
    "sunday": "День недели воскресенье, выходной день, подготовка к новой неделе"
}


def get_info_day_week(request, day: str):
    '''Информация о дне недели'''
    if day in dict_days_of_week:
        return HttpResponse(dict_days_of_week[day])
    return HttpResponseNotFound(f'Неверный номер дня - {day}')


def get_info_day_week_num(request, day: int):
    '''Перенаправление на get_info_day_week'''
    lst_days_of_week = list(dict_days_of_week)
    if day <= len(lst_days_of_week):
        day_num = lst_days_of_week[day - 1]
        redirect_url = reverse('get_info_day_week', args=[day_num])
        return HttpResponseRedirect(redirect_url)
    return HttpResponseNotFound(f'Неверный номер дня недели - {day}')
