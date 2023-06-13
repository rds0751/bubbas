from django.core.management.base import BaseCommand
from ads.models import *
from django.core.files.temp import NamedTemporaryFile
from django.core import files
from ads.models import Ad
import random
import os
import uuid
from django.core.files import File


class Command(BaseCommand):
    args = "<filename>"
    help = "Loads the initial data in to database"


    
    def handle(self, *args, **options):
        ads = Ad.objects.all()
        images = os.listdir('./medias')
        imas = []
        for image in images:
            if '.jpg' in image:
                    imas.append(image)

        for ad in ads:
            i = ad
            rn = random.choice(imas)
            imas.remove(rn)
            print(rn)
            file = File(open('/home/ubuntu/django/bubbas/medias/'+rn, "rb"))
            i.thumbnail.save(rn, file, save=True)
            i.save()
            print(i.id) 