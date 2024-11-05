from django.db import models
from apps.employees.models import Employee


class Licenses(models.Model):
	REASONS_CHOICES = (
		('cm', 'Consulta médica'),
		('lm', 'Licença maternidade'),
		('lp', 'Licença paternidade'),
		('ot', 'Outros'),
	)

	description = models.CharField(max_length=70, verbose_name="Descrição",
	                               help_text="Descrição do motivo da ausência")
	license_type = models.CharField(max_length=3, verbose_name="Tipo do documento",
	                                 choices=REASONS_CHOICES, default="cm")
	file  = models.FileField(upload_to="licenses")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	# Relationships
	employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Colaborador")

	class Meta:
		ordering = ['employee']
		verbose_name = "Licença"
		verbose_name_plural = "Licenças"


	def __str__(self):
		return self.description
