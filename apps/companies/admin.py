from django.contrib import admin
from .models import Enterprise


class EnterpriseAdmin(admin.ModelAdmin):
    model = Enterprise
    list_display = ['name','phone', 'email']
    search_fields = ['name']

admin.site.register(Enterprise, EnterpriseAdmin)
