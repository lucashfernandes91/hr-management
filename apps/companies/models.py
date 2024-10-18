from django.db import models
from django.urls import reverse


class Enterprise(models.Model):
	name = models.CharField(max_length=70, verbose_name="Nome", help_text="Nome da Empresa", unique=True)
	email = models.CharField(max_length=80, verbose_name="E-mail", help_text="E-mail de contato", unique=True)
	phone = models.CharField(max_length=15, verbose_name="Telefone", help_text="Telefone de contato", unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['name']
		verbose_name = "Empresa"
		verbose_name_plural = "Empresas"


	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('home')
