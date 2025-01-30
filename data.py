import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Results.settings')
import django
django.setup()
import random
from faker import Faker
from testapp.models import *
fake=Faker()
def Student_Fakedata(n):
    for i in range(n):
        fname = fake.name()
        froll = fake.random.randint(2425500,24255911)
        fenglish = fake.random.randint(0,100)
        fsanskrit= fake.random.randint(0,100)
        fmaths1a = fake.random.randint(0, 75)
        fmaths1b = fake.random.randint(0, 75)
        fphysics = fake.random.randint(0, 60)
        fchemistry = fake.random.randint(0, 60)


        _, created = student_results.objects.get_or_create(name=fname, rollno=froll, english=fenglish,sanskrit=fsanskrit,maths1a=fmaths1a,maths1b=fmaths1b,physics=fphysics,chemistry=fchemistry)
        if created:
            print("Data inserted successfully")
Student_Fakedata(100)
