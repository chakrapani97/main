from django.db import models

# Create your models here.
class student_results(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    english=models.IntegerField()
    sanskrit = models.IntegerField()
    maths1a = models.IntegerField()
    maths1b = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()