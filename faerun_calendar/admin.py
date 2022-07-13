from django.contrib import admin
from .models import CalendarData
from .models import MonthData
from .models import Event

admin.site.register(CalendarData)
admin.site.register(MonthData)
admin.site.register(Event)
