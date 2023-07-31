from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import datetime_safe

class StaticSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    lastmod = datetime_safe.datetime.now()
    protocol = 'https'

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home']

    def location(self, item):
        return reverse(item)
