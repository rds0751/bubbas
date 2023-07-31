from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ads.models import City, Ad
from django.utils import datetime_safe

class CallGirlAdsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    lastmod = datetime_safe.datetime.now()
    protocol = 'https'

    def items(self):
        return Ad.objects.filter(profile_status='Call Girls')

    def location(self, item):
        return reverse('call-girls:profiles', args=[item.city.slug, item.slug, item.id*28474567, ])
    

class CallGirlsCitySitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'

    def items(self):
        return City.objects.filter()

    def location(self, item):
        return reverse('call-girls:cities', args=[item.slug])