import datetime

from django.shortcuts import render


def home(request):
    print(request.POST)
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', _context)
