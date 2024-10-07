from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=70, help_text="Nome da empresa")
    email = models.CharField(max_length=80, help_text="E-mail de contato")
    phone = models.CharField(max_length=15, help_text="Telefone de contato")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


    def __str__(self):
        return self.name
