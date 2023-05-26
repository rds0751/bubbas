from django.urls import path
from .views import *

urlpatterns = [
    path('<city>/<slug>/', ad, name = 'post'),
    path('<city>/', ad, name = 'post'),
]