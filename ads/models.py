from django.db import models
from django.db.models import Q, Count, F

from django.utils.text import slugify
from ckeditor.fields import RichTextField
from pictures.models import PictureField



# Create your models here.

STATUS_TYPES = (
    ("Enabled", "Enabled"),
    ("Disabled", "Disabled"),
)

PROFILE_STATUS = (
    ("Call Girls", "Call Girls"),
    ("Escorts", "Escorts"),
) 

class Agency(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Agencies"

class Image(models.Model):
    title = models.CharField(max_length=20)
    alt_text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class Country(models.Model):
    name = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS_TYPES, max_length=10, default="Enabled")
    slug = models.SlugField(max_length=500, default="")

    def __str__(self):
        return self.name

    def get_no_of_cg_ads(self):
        return Ad.objects.filter(city__state__country=self, status="Live")
    
    
    def get_no_of_es_ads(self):
        return Ad.objects.filter(city__state__country=self, status="Live")
    
    class Meta:
        verbose_name_plural = "Countries"

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    status = models.CharField(choices=STATUS_TYPES, max_length=10, default="Enabled")
    slug = models.SlugField(max_length=500, default="")

    def __str__(self):
        return self.name

    def get_no_of_ads(self):
        return Ad.objects.filter(
            location__in=City.objects.filter(state=self), status="Live"
        )

    def get_state_cities(self):
        cities = (
            self.state.annotate(num_posts=Count("locations"))
            .filter(status="Enabled")
            .exclude(name=F("state__name"))
            .order_by("-num_posts")
        )
        return cities[:5]
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(State, self).save(*args, **kwargs)

class City(models.Model):
    name = models.CharField(max_length=500)
    state = models.ForeignKey(State, related_name="state", on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(choices=STATUS_TYPES, max_length=10, default="Enabled", null=True, blank=True)
    slug = models.SlugField(max_length=500, null=True, blank=True)
    meta_title = models.TextField(default="", null=True, blank=True)
    meta_description = models.TextField(default="", null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    call_girls_page_content = RichTextField(null=True, blank=True)
    escorts_page_content = RichTextField(null=True, blank=True)
    get_no_of_cg_ads = models.IntegerField(default=0)
    get_no_of_es_ads = models.IntegerField(default=0)
    parent_city = models.ForeignKey(
        "self",
        related_name="child_cities",
        null=True,
        blank=True,
        on_delete=models.CASCADE, 
        )

    def __str__(self):
        return self.name

    def get_ad_url(self):
        job_url = "/call-girls/" + str(self.slug) + "/"
        return job_url
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)
     
    class Meta:
        verbose_name_plural = "Cities"
    
class Ad(models.Model):
    id = models.BigAutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=10000, null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    profile_status = models.CharField(choices=PROFILE_STATUS, max_length=25, default="Enabled", null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    thumbnail = PictureField(null=True, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    featured = models.BooleanField(null=True, blank=True)
    sponsored = models.BooleanField(default=False)
    views = models.IntegerField(default=0, null=True, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    meta_title = models.TextField(default="", null=True, blank=True)
    meta_description = models.TextField(default="", null=True, blank=True)
    user = models.CharField(max_length=100, default='rds0752')
    rank = models.IntegerField(default=10)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        city = self.city
        if self.profile_status == 'Escorts':
            city.get_no_of_es_ads += 1
            city.save()
        else:
            city.get_no_of_cg_ads += 1
            city.save()
        super(Ad, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Ads"
        indexes = [models.Index(fields=['city', 'profile_status', ]), ]