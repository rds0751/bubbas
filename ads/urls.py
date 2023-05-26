from django.urls import path
from .views import *

urlpatterns = [
    path('', ad, name='home'),
    path('<slug>/', ad, name = 'post'),
]