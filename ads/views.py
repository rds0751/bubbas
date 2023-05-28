from django.shortcuts import render

# Create your views here.
from .models import Image, Ad, City, Category

# Create your views here.
def home(request):
    c = City.objects.all().order_by('?')
    ca = Category.objects.all().order_by('?')[:50]
    p = Ad.objects.all().order_by('?')[:30]
    meta_title = 'i am title of my meta'
    meta_description = 'describe my meta'
    context = {
        'cities': c,
        'categories': ca,
        'ads': p,
        'meta_title': meta_title,
        'meta_description': meta_description,
        
    }
    print(context)
    return render(request, 'home.html', context)


# Create your views here.
def city(request, city):
    city = City.objects.get(name__icontains=city)
    posts = Ad.objects.filter(city=city).order_by('?')
    c = City.objects.all().order_by('?')
    ca = Category.objects.all().order_by('?')[:50]
    p = Ad.objects.all().order_by('?')[:30]
    meta_title = 'i am title of my meta'
    meta_description = 'describe my meta'
    context = {
        'cities': c,
        'categories': ca,
        'ads': p,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'posts': posts
    }
    return render(request, 'city.html', context)

# Create your views here.
def ad(request, slug, city):
    city = City.objects.get(name__icontains=city)
    posts = Ad.objects.filter(city=city).order_by('?')[:4]
    posts1 = Ad.objects.filter(city=city).order_by('?')[:4]
    posts2 = Ad.objects.filter(city=city).order_by('?')[:4]
    post = Ad.objects.get(slug__icontains=slug)
    context = {
        'post': post,
        'posts': posts
    }
    return render(request, 'ad.html', context)