from django.shortcuts import render

# Create your views here.
from .models import Image, Ad

# Create your views here.
def home(request):
    # post = Ad.objects.get(id='UN0BRKCTHM')
    # context = {
    #     'post': post,
    # }
    return render(request, 'home.html')


# Create your views here.
def city(request, city):
    post = Ad.objects.get(id='UN0BRKCTHM')
    context = {
        'post': post,
    }
    return render(request, 'city.html', context)

# Create your views here.
def ad(request, slug, city):
    post = Ad.objects.get(id='UN0BRKCTHM')
    context = {
        'post': post,
    }
    return render(request, 'ad.html', context)