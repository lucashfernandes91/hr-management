from django.db import models


class Documents(models.Model):
    REASONS_CHOICES =  (
        ('m', 'Consulta médica'),
        ('l', 'Licença Paternidade'),
        ('a', 'Aniversário'),
        ('o', 'outros'),
    )

    description = models.CharField(max_length=70, help_text="Descrição do motivo da ausência")
    document_type = models.CharField(max_length=3, choices=REASONS_CHOICES, default="m")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
