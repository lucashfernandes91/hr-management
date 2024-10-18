from django.contrib.auth.models import User
from django.db import models
from apps.departments.models import Departments
from apps.companies.models import Enterprise


class Employee(models.Model):
	name = models.CharField(max_length=70, verbose_name="Nome", help_text="Nome do colaborador", unique=True)
	email = models.CharField(max_length=80, verbose_name="E-mail", help_text="E-mail de contato", unique=True)
	phone = models.CharField(max_length=15, verbose_name="Telefone", help_text="Telefone de contato", unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	# Relationships
	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
	departments = models.ManyToManyField(Departments, verbose_name="Departamentos", null=True, blank=True)
	enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, verbose_name="Empresa", null=True, blank=True)


	class Meta:
		ordering = ['name']
		verbose_name = "Colaborador"
		verbose_name_plural = "Colaboradores"


	def __str__(self):
		return self.name
