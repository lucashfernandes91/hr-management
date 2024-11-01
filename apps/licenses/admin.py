from django.contrib import admin
from .models import Licenses


class LicensesAdmin(admin.ModelAdmin):
    model = Licenses
    list_display = [ 'employee', 'license_type', 'description']
    search_fields = ['employee']
    
admin.site.register(Licenses, LicensesAdmin)
