from django.shortcuts import render
from django.http import HttpResponse
from .models import icecream_db

def icecream_list(request):
    icecream = ''
    for i in range(len(icecream_db)):
        icecream += icecream_db[i]['name']+'::'
    return HttpResponse(f'Список сортов мороженого: {icecream}')


