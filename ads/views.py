from django.shortcuts import render

# Create your views here.
from .models import Image, Ad

# Create your views here.
def ad(request):
    post = Ad.objects.get(id='UN0BRKCTHM')
    context = {
        'post': post,
    }
    return render(request, 'city.html', context)