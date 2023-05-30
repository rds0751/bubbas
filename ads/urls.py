from django.urls import path
from .views import *

urlpatterns = [
    path('<city>/', city, name = 'post'),
    path('<city>/<slug>/', ad, name = 'post'),
]