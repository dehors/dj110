from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado

# Create your views here.
def inicio(request):
	title = "titulo"
	if request.user.is_authenticated():
		title = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)
	context = {
		"el_form": form,
		"title":title,
	}
	if form.is_valid():
		print(form.cleaned_data)
		instance = form.save(commit=False)# commit=False impide que se guarde para poder hacer otra cosa
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = 'persona'
		instance.save()
		context = {
			"title":"Gracias %s!" %(nombre),
		}
		if not nombre:
			context = {
				"title": "Gracias persona sin nombre %s!" %(email)
			}
		print instance
		print instance.timestamp
		#form_data = form.cleaned_data
		# print form_data.get("email")
		#abc = form_data.get("email")
		#obj = Registrado.objects.create(email=abc, nombre = form_data.get("nombre"))

		#obj = Registrado()
		#obj.email = abc
		#obj.save()
	# print(dir(form)) ver metodos del form
	return render(request, "inicio.html", context)
