from django.contrib import admin
from .models import *

# Register your models here.
class student_results_admin(admin.ModelAdmin):
    list_display = ['rollno','name','english','sanskrit','maths1a','maths1b','physics','chemistry']

admin.site.register(student_results,student_results_admin)