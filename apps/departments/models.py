from django.db import models


class Departments(models.Model):
	name = models.CharField(max_length=70, verbose_name="Departamento", help_text="Nome do Departamento")
	email = models.CharField(max_length=80, verbose_name="E-mail", help_text="E-mail de contato")
	phone = models.CharField(max_length=15, verbose_name="Telefone", help_text="Telefone de contato")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['name']
		verbose_name = "Departamento"
		verbose_name_plural = "Departamentos"


	def __str__(self):
		return self.name
