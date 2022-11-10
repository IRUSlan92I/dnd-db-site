from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import YearData
from .models import MonthData
from .models import CalendarData
from .models import Event


def day_page(request, year: int, month: int, day: int):
    params = None

    select_suggested = False
    select_only_for_gm = False

    if not params:
        try:
            year_data = YearData.objects.get(number=year)
        except YearData.DoesNotExist:
            params = {'type': 'error', 'error_type': 'year'}

    if not params:
        try:
            year_id = getattr(year_data, 'id')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'year'}

    if not params:
        try:
            month_data = MonthData.objects.get(number=month)
        except MonthData.DoesNotExist:
            params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            month_id = getattr(month_data, 'id')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            is_leap = getattr(year_data, 'is_leap')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'year'}
        else:
            try:
                is_leap_month = getattr(month_data, 'is_leap_month')
            except AttributeError:
                params = {'type': 'error', 'error_type': 'month'}
            else:
                if not is_leap and is_leap_month:
                    params = {'type': 'error', 'error_type': 'month'}

    if not params:
        try:
            events = Event.objects.filter(year=year_id, month=month_id, day=day,
                                          is_suggested=select_suggested, is_only_for_gm=select_only_for_gm
                                          ).order_by('time')
        except Event.DoesNotExist:
            params = {'type': 'error', 'error_type': 'events'}

    if not params:
        try:
            is_oneday = getattr(month_data, 'is_oneday')
        except AttributeError:
            params = {'type': 'error', 'error_type': 'month'}
        else:
            if is_oneday and day != 1 or not 1 <= day <= 30:
                params = {'type': 'error', 'error_type': 'day'}

    if not params:
        params = {
            'type': 'day',
            'root': '',
            'year_data': year_data,
            'month_data': month_data,
            'day': day,
            'events': events,
        }

    return render(request, 'faerun_calendar/index.html', params)


def year_page(request, year: int):
    params = None

    try:
        year_data = YearData.objects.get(number=year)
    except YearData.DoesNotExist:
        params = {'type': 'error', 'error_type': 'year'}

    if not params:
        try:
            month_data = MonthData.objects.all().order_by('number')
            calendar_data = CalendarData.objects.first()

            months = []
            for month in month_data:
                is_oneday_month = getattr(month, 'is_oneday')
                is_leap_month = getattr(month, 'is_leap_month')
                is_leap_year = getattr(year_data, 'is_leap')

                if is_leap_month and not is_leap_year:
                    continue
                m = {
                    'id': getattr(month, 'id'),
                    'number': getattr(month, 'number'),
                    'name': getattr(month, 'name'),
                    'folkname': getattr(month, 'folkname'),
                    'is_oneday': getattr(month, 'is_oneday'),
                    'days': []
                }
                for i in range(0, 1 if is_oneday_month else 30):
                    day = {
                        'number': i+1,
                        'event_counts': Event.objects.filter(year=year_data.id, month=month.id, day=i+1,
                                                             is_suggested=False, is_only_for_gm=False).count()
                    }
                    m['days'].append(day)

                months.append(m)

            params = {
                'type': 'year',
                'root': '../',
                'calendar_data': calendar_data,
                'year_data': year_data,
                'months': months,
            }
        except AttributeError:
            params = {'type': 'error', 'error_type': 'unknown'}

    return render(request, 'faerun_calendar/index.html', params)


def index(request):
    try:
        current_year = getattr(getattr(CalendarData.objects.first(), 'current_year'), 'number')
    except AttributeError:
        current_year = 0

    return HttpResponseRedirect(f'{current_year}')
