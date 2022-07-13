from django.shortcuts import render
from .models import Link


def index(request):
    links = Link.objects.order_by('order')

    return render(request, 'links/index.html', {'links': links})
