from django.forms import ModelForm
from . import models


class StudentForm(ModelForm):
    class Meta:
    	model = models.Student
    	fields = ['name', 'image', 'roll', 'registration', 'phone', 'session_start', 'session_end', 'department', 'klass', 'parent']



