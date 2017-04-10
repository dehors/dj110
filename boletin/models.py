from django.db import models

from django.db import models

# Create your models here.
class Registrado(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self): #python 2
		return self.email

	def __srt__(self): #python 3
		return self.email