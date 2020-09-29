from django import forms
from .models import Email



class ContactModelForm(forms.ModelForm):
	class Meta:
		model = Email
		fields = ['Client','Addmail','sujet','description']