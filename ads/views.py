from django.shortcuts import render

# Create your views here.
from ads.models import Image, Ad, City, Category
from home.models import Data

# Create your views here.
def home(request):
    c = City.objects.all().order_by('?')
    ca = Category.objects.all().order_by('?')[:50]
    p = Ad.objects.filter(featured=True).order_by('?')[:30]
    ad_count = Ad.objects.all().count()
    meta_title = Data.objects.get(key='home_meta_title').value.replace('%ad_count', str(ad_count))
    meta_description = Data.objects.get(key='home_meta_description').value
    site_name = Data.objects.get(key='site_name').value
    site_logo = Data.objects.get(key='site_logo')
    context = {
        'cities': c,
        'categories': ca,
        'ads': p,
        'meta_title': meta_title, 
        'meta_description': meta_description,
        'site_logo': site_logo,
        'site_name': site_name
    }
    print(context)
    return render(request, 'home.html', context)