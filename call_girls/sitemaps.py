from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ads.models import City, Ad

class CallGirlAdsSitemap(Sitemap):

    def items(self):
        return Ad.objects.filter()

    def location(self, item):
        return reverse('call-girls:profiles', args=[item.city.slug, item.slug, item.id*28474567, ])
    

class CallGirlsCitySitemap(Sitemap):

    def items(self):
        return City.objects.filter()

    def location(self, item):
        return reverse('call-girls:cities', args=[item.slug])