from django.shortcuts import render
from .models import Vacancy
from .forms import FindForm
import datetime


# Create your views here.
def home_view(request):
    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    date = datetime.datetime.now().date()
    name = 'Dave'
    _content = {'object_list': qs, 'date': date, 'name': name, 'form': form}
    return render(request, 'scraping/home.html', _content)


def view_all_vacancy(request):
    qs = Vacancy.objects.all()
    date = datetime.datetime.now().date()
    name = 'Dave'
    _content = {'object_list': qs, 'date': date, 'name': name}
    return render(request, 'scraping/view_all_vacancy.html', _content)
