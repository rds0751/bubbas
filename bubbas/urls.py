"""bubbas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'), name='')
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from ads.views import home, all
from pictures.conf import get_settings
from django.contrib.sitemaps import views
from flatpages.sitemaps import FlatPageSitemap
from call_girls.sitemaps import CallGirlsCitySitemap, CallGirlAdsSitemap
from escorts.sitemaps import EscortsCitySitemap, EscortsAdsSitemap
from .sitemaps import StaticSitemap

sitemaps = {
 'call-girls-cities': CallGirlsCitySitemap,
 'call-girls-profiles': CallGirlAdsSitemap,
 'escorts-cities': EscortsCitySitemap,
 'escorts-profiles': EscortsAdsSitemap,
 'static-pages': FlatPageSitemap,
 'home-page': StaticSitemap
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('call-girls/', include('call_girls.urls', 'call-girls')), # new
    path('escorts/', include('escorts.urls', 'escorts')), # new
    path('pages', include('flatpages.urls'), name='static'),
    path('', home, name='home'),
    path('all-locations/', all, name='all'),
    path('__debug__/', include('debug_toolbar.urls'), name=''),
    path("cookies/", include("cookie_consent.urls"), name=''),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('accounts/', include('account.urls')),
    path('ads/', include('ads.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("_pictures/", include("pictures.urls")),
    ]


from django.core.files.temp import NamedTemporaryFile
from django.core import files
from ads.models import Ad
import random
import os
import uuid
from django.core.files import File

ads = Ad.objects.all()
images = os.listdir('./medias')
imas = []
for image in images:
      if '.jpg' in image:
            imas.append(image)

for ad in ads:
    i = ad
    rn = random.choice(imas)
    imas.remove(rn)
    print(rn)
    file = File(open('/home/ubuntu/django/bubbas/medias/'+rn, "rb"))
    i.thumbnail.save(rn, file, save=True)
    i.save()
    print(i.id)
    image_temp_file = NamedTemporaryFile(delete=True)
    in_memory_image = open('/home/ubuntu/django/bubbas/medias/'+rn, 'rb')
    print(in_memory_image)
    for block in in_memory_image.read(1024 * 8):
            print('1')
            if not block:
                    print('2')
                    break
            print('3')
            image_temp_file.write(block)
            print('4')
    file_name = rn
    image_temp_file.flush()
    temp_file = files.File(image_temp_file, name=file_name)
    i.thumbnail = temp_file
    i.thumbnail.save(rn, in_memory_image, save=True)
    i.save()
    print(i.id)