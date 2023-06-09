from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home']

    def location(self, item):
        return reverse(item)
