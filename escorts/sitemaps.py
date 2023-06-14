from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from ads.models import City, Ad

class EscortsAdsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Ad.objects.filter(profile_status="Escorts")

    def location(self, item):
        return reverse('escorts:profiles', args=[item.city.slug, item.slug, item.id*28474567, ])
    

class EscortsCitySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return City.objects.filter()

    def location(self, item):
        return reverse('escorts:cities', args=[item.slug])