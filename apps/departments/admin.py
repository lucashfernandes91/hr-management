from django.contrib import admin
from .models import Departments

class DepartmentAdmin(admin.ModelAdmin):
    model = Departments
    list_display = ['name', 'email', 'phone']
    search_fields = ['name']

admin.site.register(Departments, DepartmentAdmin)
