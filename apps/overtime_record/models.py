from django.db import models
from apps.employees.models import Employee


class OvertimeRecord(models.Model):
	reason = models.CharField(max_length=100, verbose_name="Motivo", help_text="Qual o motivo para a hora extra?")
	hours = models.CharField(max_length=5, verbose_name="Horas trabalhadas", help_text="Quantidade de horas trabalhadas?")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	# Relationships
	employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name="Colaborador", null=True)

	class Meta:
		ordering = ['created_at', 'hours']
		verbose_name = "Hora extra"
		verbose_name_plural = "Hora extra"

	def __str__(self):
		return self.reason