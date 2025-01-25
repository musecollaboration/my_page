from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


dict_days_of_week = {
    "monday": "День недели понедельник, будний день начало недели",
    "tuesday": "День недели вторник, будний день второй день недели",
    "wednesday": "День недели среда, будний день середина недели",
    "thursday": "День недели четверг, будний день преддверие выходных",
    "friday": "День недели пятница, будний день конец рабочей недели",
    "saturday": "День недели суббота, выходной день, время отдыха",
    "sunday": "День недели воскресенье, выходной день, подготовка к новой неделе"
}


def get_info_day_week(request, day):
    if day in dict_days_of_week:
        return HttpResponse(dict_days_of_week[day])
    return HttpResponseNotFound(f'Неверный номер дня - {day}')
