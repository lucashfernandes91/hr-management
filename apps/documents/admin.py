from django.contrib import admin
from .models import Documents


class DocumentsAdmin(admin.ModelAdmin):
	model = Documents
	list_display = [ 'employee', 'document_type', 'description']
	search_fields = ['employee']
	
admin.site.register(Documents, DocumentsAdmin)
