from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from .forms import StudentResultsForm
# Create your views here.

def insert_view(request):
    form = StudentResultsForm()
    if request.method == 'POST':
        form = StudentResultsForm(request.POST)
        if form.is_valid():
            rollno = form.cleaned_data['rollno']
            if not student_results.objects.filter(rollno=rollno).exists():
                form.save()
                return HttpResponse('<h1>Data inserted Sucessfully</h1>')
            else:
                form.add_error('rollno', 'Roll number already exists')
    else:
        form = StudentResultsForm()  # Reinitialize an empty form
    return render(request, 'testapp/insert.html', {'form': form})


from .forms import StudentResultsForm
from django.shortcuts import render, get_object_or_404
from .models import student_results

def search_view(request):
    if request.method == 'POST':
        rollno = request.POST.get('rollno')
        student = get_object_or_404(student_results, pk=rollno)
        student_total_marks = student.english + student.sanskrit + student.maths1a + student.maths1b + student.physics + student.chemistry
        return render(request, 'testapp/results.html', {'student': student,'student_total_marks':student_total_marks})
    return render(request, 'testapp/search.html')