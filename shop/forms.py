from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Submit

class ProductCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ProductCreateForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-4 mt-2'
		self.helper.field_class = 'col-lg-8 mt-2'
		self.helper.add_input(Submit('submit', 'Ajouter'))


	class Meta:
		model = Product
		fields = '__all__'