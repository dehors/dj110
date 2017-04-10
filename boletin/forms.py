from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["email","nombre"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("ingrese un correo de USC")
		if not extension == "edu":
			raise forms.ValidationError("Porfavor ingrese una direccion de correo valida ")
		return email

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not domain == 'USC':
			raise forms.ValidationError("ingrese un correo de USC")
		if not extension == "edu":
			raise forms.ValidationError("Porfavor ingrese una direccion de correo valida ")
		return email