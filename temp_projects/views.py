from django.shortcuts import render
from django.http import HttpResponse


people = [
    'Жукова Анна Константиновна',
    'Юлия Степановна Потапова',
    'Гущин Аполлинарий Тимурович',
    'Дорофей Ярославович Третьяков',
    'Селезнева Анна Тарасовна',
    'Федотов Симон Харлампьевич',
    'Красильникова Вера Борисовна',
    'Бажен Тихонович Костин',
    'Веселова Анжелика Тимофеевна',
    'Щербаков Самсон Феодосьевич'
]

people2 = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]


def index(request):
    return render(request, 'temp_projects/index.html')


def sample1(request):
    context = {
        'year_born': 1964,
        'city_born': 'Бейруте',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'temp_projects/sample1.html', context=context)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': "Bobs' BBQ & Grill",
        'count_needle': 1790,
    }
    return render(request, 'temp_projects/guinnessworldrecords.html', context=context)


def get_info_people(request):
    contex = {
        'people': people
    }
    return render(request, 'temp_projects/people.html', context=contex)


def get_info_people_detail(request):
    context = {
        'people2': people2
    }
    return render(request, 'temp_projects/people_detail.html', context=context)


def get_table(request):
    return render(request, 'temp_projects/table.html')
