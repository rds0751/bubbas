from django.shortcuts import render

# Create your views here.
from ads.models import Ad, City, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import Data

# Create your views here.
def city(request, city):
    city = City.objects.get(slug=city)
    posts = Ad.objects.filter(city=city, profile_status='Call Girls').order_by('?')
    c = City.objects.all().order_by('?')
    ca = Category.objects.all().order_by('?')[:50]
    p = Ad.objects.all().order_by('?')[:30]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        print(request.session["accepted_cookies"])
    except Exception as e:
        request.session["accepted_cookies"] = False
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    if city.meta_title:
        meta_title = city.meta_title
    else:
        meta_title = str(city.get_no_of_cg_ads) + ' ' + str(city.name) + ' Call Girls & ' + str(int(city.get_no_of_cg_ads*2.30865)) + ' Photos with Whatsapp Number'
    if city.meta_description:
        meta_description = city.meta_description
    else:
        meta_description = 'Find ' + str(city.name) + ' call girls with Real Photos and Number Incall & Outcall pick and drop service at Bubbas has all the latest ads on '+ str(city.name) +', updated every day.'
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
    city = City.objects.get(slug=city)
    try:
        print(request.session["accepted_cookies"])
    except Exception as e:
        request.session["accepted_cookies"] = False
    posts = Ad.objects.filter(city=city, profile_status='Call Girls').order_by('?')[:4]
    posts1 = Ad.objects.filter(city=city, profile_status='Call Girls').order_by('?')[:4]
    posts2 = Ad.objects.filter(city=city, profile_status='Call Girls').order_by('?')[:4]
    post = Ad.objects.get(slug=slug)
    meta_title = post.title
    meta_description = post.overview
    context = {
        'post': post,
        'posts': posts,
        'meta_title': meta_title,
        'meta_description': meta_description

    }
    return render(request, 'ad.html', context)