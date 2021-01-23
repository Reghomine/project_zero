from django.shortcuts import render
from django.http import HttpResponse
from .models import icecream_db

def icecream_list(request):
    icecream = ''
    for i in range(len(icecream_db)):
        icecream += f"<a href = '{i}'>{icecream_db[i]['name']}</a><br>"
    context = {'icecream':icecream}
    return render(request, 'icecream/icecream-list.html', context)

