from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ads.models import City, Ad

class EscortsAdsSitemap(Sitemap):

    def items(self):
        return Ad.objects.filter(profile_status="Escorts")

    def location(self, item):
        return reverse('call-girls:profiles', args=[item.city.slug, item.slug, item.id*28474567, ])
    

class EscortsCitySitemap(Sitemap):

    def items(self):
        return City.objects.filter()

    def location(self, item):
        return reverse('call-girls:cities', args=[item.slug])