from django.core.management.base import BaseCommand
from ads.models import *


class Command(BaseCommand):
    args = "<filename>"
    help = "Loads the initial data in to database"


    
    def handle(self, *args, **options):
        
        cities = ["Agra","Ahmedabad","Ajmer","Allahabad","Ambala","Amritsar","Bangalore","Bhopal","Bhubaneswar","Chandigarh","Chennai","Dehradun","Delhi","Faridabad","Ghaziabad","Goa","Greater Noida","Gurgaon","Guwahati","Hyderabad","Indore","Jaipur","Jalandhar","Jamshedpur","Jodhpur","Kanpur","Kochi","Kolkata","Kota","Lucknow","Ludhiana","Manali","Manesar","Mohali","Mumbai","Nagpur","Nainital","Nashik","Navi Mumbai","Noida","Panchkula","Patna","Pune","Raipur","Rajkot","Ranchi","Rishikesh","Shimla","Surat","Thane","Udaipur","Vadodara","Vijayawada","Zirakpur"]
        categories = ["69","Adult Baby Minding","A Level - Anal","BDSM","Bisexual","Blowjob","Bukkake","Car Meets","CIF - Cum in Face","COB","Couples","Crossdresser","CIM - Cum in Mouth","Deep Throat","Dogging","Domination","DUO","Erotic massage","Face Sitting","Fetish","Filming","Fisting","French Kiss","Gang Bang","GFE","Hardcore sex","HDJ - Handjob","Incall","Kissing","Massage","Milking/Lactating","Outcall","OW","OWO","Party Girl","Pregnant","PSE - Pornstar","Quickie","Rimming","Rimming (giving)","Role-playing","Hardsports & Scat","Spanking","Squirting","Pegging - Strapon","Submissive","Swallow","Threesomes","Tie and Tease","Travel","Uniform","Watersports"]
        url = "ls-da7a92b0797c88d3459343bcb1d7c69ce6cd65ab.cfcmo0to43fn.ap-south-1.rds.amazonaws.com"
        for x in categories:
            print(x)
            c = Category()
            c.title = x
            c.save()

