from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registrado

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode__","nombre","timestamp"]
	list_filter = ["timestamp"]
	list_editable = ["nombre"]
	search_fields = ["email","nombre"]
	form = RegModelForm
	#class Meta:
		#model = Registrado

admin.site.register(Registrado,AdminRegistrado)