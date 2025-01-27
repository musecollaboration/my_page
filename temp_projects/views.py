from django.shortcuts import render


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
