from django import template

register = template.Library()


@register.filter(name='my_range')
def my_range(value):
    res = [value for i in range(10)]
    return res


@register.filter(name='my_range_num')
def my_range_num(value):
    res = [i for i in range(10)]
    return res


@register.filter(name='times')
def times(key):
    res = [i for i in range(key)]
    return res


@register.filter(name='filter_range')
def filter_range(start, stop):
    res = [i for i in range(start, stop)]
    return res
