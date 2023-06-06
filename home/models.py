from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Data(models.Model):
    key    = models.CharField(max_length=100, null=True, blank=True)
    value  = RichTextField(null=True, blank=True)
    status = models.CharField(max_length=25, default="Enabled", null=True, blank=True)
    image  = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Data"
        indexes = [models.Index(fields=['key',]), ]

    def __str__(self):
        return self.key
    
class Sitemap(models.Model):
    url = models.CharField(max_length=500, default='')
    parent_url = models.ForeignKey(Sitemap, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now_add=True)