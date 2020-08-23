from django.shortcuts import render, redirect
from . import models
from . import forms

# Create your views here.
def student_list(request):
    student = models.Student.objects.all()        # '-techer_id' for ascending order
    context = {
        'student': student,
    }
    return render(request, 'student/student_list.html', context)