from django.contrib import admin
from .models import *


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]


class AdAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('categories', 'images',)
    exclude = ('views', 'likes')

admin.site.register(Image, imageAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Agency)