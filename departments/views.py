from django.shortcuts import render, redirect,HttpResponseRedirect
from . import models
from .forms import DepartmentForm
from django.urls import reverse


# Create your views here.
def department_list(request):
    department = models.Department.objects.all()        # '-techer_id' for ascending order
    context = {
        'department': department,
    }
    return render(request, 'departments/departments_list.html', context)




def add_department(request,template_name='departments/departments_forms.html'):

        success_url = reverse('department_list')

        department_qs = models.Department.objects.all()

        if request.method == 'POST':
            form = DepartmentForm(request.POST)
            if form.is_valid():
                # with transaction.atomic():
                form.save()
                return HttpResponseRedirect(success_url)

        else:
            form = DepartmentForm()
        context = {'form':form,'title':"Add department"}
        return render(request, template_name,context )



def edit_department(request,pk,template_name='departments/departments_forms.html'):

        success_url = reverse('department_list')

        instance = models.Department.objects.get(pk=pk)
        if request.method == "POST":
            form = DepartmentForm(request.POST, instance=instance)
            if form.is_valid():
                # with transaction.atomic():
                form.save()
                return HttpResponseRedirect(success_url)
        else:
            form = DepartmentForm(instance=instance)
        context = {'form':form,'title':"Update department"}
        return render(request, template_name,context)



def delete_department(request, pk):

        success_url = reverse('department_list')

        department = models.Department.objects.get(pk=pk)
        department.delete()
        messages.error(request,"Successfully Deleted department ")
        return HttpResponseRedirect(success_url)