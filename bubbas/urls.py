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
from ads.views import home
from pictures.conf import get_settings
from django.contrib.sitemaps import views
from flatpages.sitemaps import FlatPageSitemap
from call_girls.sitemaps import CallGirlsCitySitemap, CallGirlAdsSitemap
from escorts.sitemaps import EscortsCitySitemap, EscortsAdsSitemap

sitemaps = {
 'call-girls-cities': CallGirlsCitySitemap,
 'call-girls-profiles': CallGirlAdsSitemap,
 'escorts-cities': EscortsCitySitemap,
 'escorts-profiles': EscortsAdsSitemap,
 'static-pages': FlatPageSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('call-girls/', include('call_girls.urls', 'call-girls')), # new
    path('escorts/', include('escorts.urls', 'escorts')), # new
    path('pages/', include('flatpages.urls'), name='static'),
    path('', home, name='home'),
    path('__debug__/', include('debug_toolbar.urls'), name=''),
    path("cookies/", include("cookie_consent.urls"), name=''),
    path('sitemap.xml', views.index, {'sitemaps': sitemaps}),
    path('sitemap-<section>.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("_pictures/", include("pictures.urls")),
    ]