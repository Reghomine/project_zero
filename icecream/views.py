from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Icecream

def icecream_list(request):
    icecream = Icecream.objects.all()
    
    context = {'icecream':icecream}
    return render(request, 'icecream/icecream-list.html', context)

def icecream_detail(request, pk):
    icecream = get_object_or_404(Icecream, pk=pk)
    rating = int(icecream.rating)
    context = {
        'icecream':icecream,
        'range':range(rating),
        'zero_range':range(5-rating),
    }
    return render(request, 'icecream/icecream-detail.html', context)