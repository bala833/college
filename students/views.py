from django.shortcuts import render, redirect,HttpResponseRedirect
from . import models
from .forms import StudentForm
from django.urls import reverse


# Create your views here.
def student_list(request):
    student = models.Student.objects.all()        # '-techer_id' for ascending order
    context = {
        'student': student,
    }
    return render(request, 'student/students_list.html', context)




def add_student(request,template_name='student/student_form.html'):

        success_url = reverse('student_list')

        student_qs = models.Student.objects.all()

        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                # with transaction.atomic():
                form.save()
                return HttpResponseRedirect(success_url)

        else:
            form = StudentForm()
        context = {'form':form,'title':"Add Student"}
        return render(request, template_name,context )



def edit_student(request,pk,template_name='student/student_form.html'):

        success_url = reverse('student_list')

        instance = models.Student.objects.get(pk=pk)
        if request.method == "POST":
            form = StudentForm(request.POST, instance=instance)
            if form.is_valid():
                # with transaction.atomic():
                form.save()
                return HttpResponseRedirect(success_url)
        else:
            form = StudentForm(instance=instance)
        context = {'form':form,'title':"Update Student"}
        return render(request, template_name,context)



def delete_student(request, pk):

        success_url = reverse('student_list')

        student = models.Student.objects.get(pk=pk)
        student.delete()
        messages.error(request,"Successfully Deleted Student ")
        return HttpResponseRedirect(success_url)