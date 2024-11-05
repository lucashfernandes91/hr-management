from django.db import models
from apps.employees.models import Employee


class Documents(models.Model):
	REASONS_CHOICES = (
		('ct', 'Carteira de trabalho'),
		('cm', 'Carteira de motorista'),
		('ot', 'Outros'),
	)

	description = models.CharField(max_length=70, verbose_name="Descrição",
	                               help_text="Descrição do documento, caso preciso")
	document_type = models.CharField(max_length=3, verbose_name="Tipo do documento",
	                                 choices=REASONS_CHOICES, default="ct")
	file  = models.FileField(upload_to="documents")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	# Relationships
	employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Colaborador")

	class Meta:
		ordering = ['employee']
		verbose_name = "Documento"
		verbose_name_plural = "Documentos"


	def __str__(self):
		return self.description
