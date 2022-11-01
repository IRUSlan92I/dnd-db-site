from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

from .models import YearData
from .models import MonthData
from .models import CalendarData
from .models import Event


def day_page(request, year: int, month: int, day: int):
    try:
        year_data = YearData.objects.get(number=year)
    except YearData.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    try:
        year_id = getattr(year_data, 'id')
    except AttributeError:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    try:
        month_data = MonthData.objects.get(number=month)
    except MonthData.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    try:
        month_id = getattr(month_data, 'id')
    except AttributeError:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    try:
        events = Event.objects.filter(year=year_id, month=month_id, day=day)
    except Event.DoesNotExist:
        return HttpResponseNotFound(f'<h1>404 Not Found</h1>')

    params = {
        'type': 'day',
        'year_data': year_data,
        'month_data': month_data,
        'day': day,
        'events': events,
    }

    return render(request, 'faerun_calendar/index.html', params)


def year_page(request, year: int):
    try:
        year_data = YearData.objects.get(number=year)
    except YearData.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')

    month_data = MonthData.objects.all()
    calendar_data = CalendarData.objects.first()
    events = Event.objects.all()

    params = {
        'type': 'year',
        'calendar_data': calendar_data,
        'year_data': year_data,
        'month_data': month_data,
        'month_days': tuple(i+1 for i in range(30)),
        'events': events,
    }

    return render(request, 'faerun_calendar/index.html', params)


def index(request):
    try:
        current_year = getattr(getattr(CalendarData.objects.first(), 'current_year'), 'number')
    except AttributeError:
        current_year = 0

    return year_page(request, current_year)
