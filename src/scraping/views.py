from django.shortcuts import render
from .models import Vacancy
import datetime


# Create your views here.
def home_view(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    qs = Vacancy.objects.all()
    _content = {'object_list': qs, 'date': date, 'name': name}
    return render(request, 'scraping/home.html', _content)

