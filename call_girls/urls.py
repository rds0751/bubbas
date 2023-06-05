from django.urls import path
from .views import *

app_name = 'call_girls'

urlpatterns = [
    path('<city>/', city, name = 'cities'),
    path('<city>/<slug>/<id>/', ad, name = 'profiles'),
]