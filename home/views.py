from django.shortcuts import render
from .models import Key
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def api(request, key):
    try:
        k = Key.objects.get(key=key)
    except Exception as e:
        return HttpResponse(str(0))
    return HttpResponse(str(1))