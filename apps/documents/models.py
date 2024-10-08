from django.db import models


# Implementar campo para upload de arquivo

class Documents(models.Model):
	REASONS_CHOICES = (
		('cm', 'Consulta médica'),
		('lp', 'Licença Paternidade'),
		('ot', 'Outros'),
	)

	description = models.CharField(max_length=70, verbose_name="Descrição",
	                               help_text="Descrição do motivo da ausência")
	document_type = models.CharField(max_length=3, verbose_name="Tipo do documento",
	                                 choices=REASONS_CHOICES, default="cm")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		# ordering = ['user'] IMPLEMENTAR RELAÇÃO
		verbose_name = "Documento"
		verbose_name_plural = "Documentos"
