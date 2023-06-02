from django.shortcuts import render

# Create your views here.
from ads.models import Image, Ad, City, Category
from home.models import Data

# Create your views here.
def home(request):
    c = City.objects.all().order_by('?')
    ad_count = Ad.objects.all()
    meta_title = Data.objects.get(key='home_meta_title').value.replace('%ad_count', str(ad_count))
    meta_description = Data.objects.get(key='home_meta_description').value
    site_name = Data.objects.get(key='site_name').value
    site_logo = Data.objects.get(key='site_logo')
    page_content = Data.objects.get(key='home_content').value
    context = {
        'cities': c,
        'meta_title': meta_title, 
        'meta_description': meta_description,
        'site_logo': site_logo,
        'site_name': site_name,
        'page_content': page_content
    }
    print(context)
    return render(request, 'home.html', context)