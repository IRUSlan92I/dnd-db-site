from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>', views.year_page, name='index'),
    path('<int:year>/<int:month>/<int:day>', views.day_page, name='index'),
]

