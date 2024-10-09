from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ['name', 'enterprise', 'phone']
    search_fields = ['name', 'enterprise']

admin.site.register(Employee, EmployeeAdmin)
