from django.forms import ModelForm
from . import models
from django import forms


class DepartmentForm(forms.ModelForm):

	def _init_(self, *args, **kwargs):
	    super(DepartmentForm, self)._init_(*args, **kwargs)  # Call to ModelForm constructor
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
	             Div('dept_head',css_class="col-md-3"),
	             Div('subject',css_class="col-md-3"),
	             css_class="row")
	        ),
	    )
	class Meta:
		model = models.Department
		fields = ['name', 'dept_head', 'subject']



