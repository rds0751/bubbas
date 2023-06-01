from django.db import models

# Create your models here.
class Data(models.Model):
    key    = models.CharField(max_length=100, null=True, blank=True)
    value  = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=25, default="Enabled", null=True, blank=True)
    image  = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.key