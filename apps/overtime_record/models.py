from django.db import models
from django.forms import ModelForm


class OvertimeRecord(models.Model):
    reason = models.CharField(max_length=100, help_text="Qual o motivo para a hora extra?")
    hours = models.CharField(max_length=5, help_text="Quantidade de horas trabalhadas?")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
