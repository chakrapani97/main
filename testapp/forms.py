from django import forms
from .models import *

class StudentResultsForm(forms.ModelForm):
    class Meta:
        model = student_results
        fields = '__all__'