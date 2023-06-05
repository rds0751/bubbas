from django.apps import apps as django_apps
from django.contrib.sitemaps import Sitemap
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse
from .models import FlatPage


class FlatPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return FlatPage.objects.filter(registration_required=False, )
    
    def location(self, item):
        return reverse('flatpages:flatpage', args=[item.url, ])