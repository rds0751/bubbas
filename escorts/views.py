from django.shortcuts import render

# Create your views here.
from ads.models import Image, Ad, City, Category
from home.models import Data

# Create your views here.
def city(request, city):
    city = City.objects.get(slug__icontains=city)
    posts = Ad.objects.filter(city=city, profile_status='Escorts').order_by('?')
    c = City.objects.all().order_by('?')
    ca = Category.objects.all().order_by('?')[:50]
    p = Ad.objects.all().order_by('?')[:30]
    if city.meta_title:
        meta_title = city.meta_title
    else:
        meta_title = str(city.get_no_of_es_ads) + ' ' + city.name + ' Escorts & ' + str(int(city.get_no_of_es_ads*2.20234)) + ' Photos with Whatsapp Number'
    if city.meta_description:
        meta_description = city.meta_description
    else:
        meta_description = 'Find ' + city.name + ' Escorts with Real Photos and Number Incall & Outcall pick and drop service at Bubbas has all the latest ads on '+ + city.name + +', updated every day.'
    context = {
        'cities': c,
        'categories': ca,
        'ads': p,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'posts': posts,
        'city': city
    }
    return render(request, 'city.html', context)

# Create your views here.
def ad(request, slug, city, id):
    city = City.objects.get(slug__icontains=city)
    posts = Ad.objects.filter(city=city, profile_status='Escorts').order_by('?')[:4]
    posts1 = Ad.objects.filter(city=city, profile_status='Escorts').order_by('?')[:4]
    posts2 = Ad.objects.filter(city=city, profile_status='Escorts').order_by('?')[:4]
    post = Ad.objects.get(slug__icontains=slug)
    context = {
        'post': post,
        'posts': posts
    }
    return render(request, 'ad.html', context)