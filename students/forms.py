from django.forms import ModelForm
from . import models
from django import forms


class StudentForm(forms.ModelForm):

	def _init_(self, *args, **kwargs):
	    super(StudentForm, self)._init_(*args, **kwargs)  # Call to ModelForm constructor
	    # for f in self.fields:
	    # 	if type(self.fields[f]) is forms.DateField:
	    # 		self.fields[f].widget.attrs['class'] = 'datepicker'
	            # self.fields[f].widget = forms.DateTimeInput(format='%Y-%m-%d  %H:%M')

	    self.helper = FormHelper()
	    self.helper.form_tag = False
	    self.helper.layout = Layout(
	        Fieldset(
	            Div(
	             Div('name',css_class="col-md-3"),
	             Div('image',css_class="col-md-3"),
	             Div('roll',css_class="col-md-3"),
	             Div('registration',css_class="col-md-3"),
	             Div('phone',css_class="col-md-3"),
	             Div('session_start',css_class="col-md-3"),
	             Div('session_end',css_class="col-md-3"),
	             Div('department',css_class="col-md-3"),
	             Div('klass',css_class="col-md-3"),
	             Div('parent',css_class="col-md-3"),
	             css_class="row")
	        ),
	    )
	class Meta:
		model = models.Student
		fields = ['name', 'image', 'roll', 'registration', 'phone', 'session_start', 'session_end', 'department', 'klass', 'parent']



