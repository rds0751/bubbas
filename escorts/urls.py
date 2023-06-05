from django.urls import path
from .views import *

app_name = 'escorts'

urlpatterns = [
    path('<city>/', city, name = 'city'),
    path('<city>/<slug>/<id>/', ad, name = 'post'),
]