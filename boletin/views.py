from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form_data = form.cleaned_data
		# print form_data.get("email")
		abc = form_data.get("email")
		obj = Registrado.objects.create(email=abc, nombre = form_data.get("nombre"))

		#obj = Registrado()
		#obj.email = abc
		#obj.save()
	# print(dir(form)) ver metodos del form
	context = {
		"el_form": form
	}
	return render(request, "inicio.html", context)
