from django.contrib import admin
from .models import OvertimeRecord


class OvertimeRecordAdmin(admin.ModelAdmin):
    model = OvertimeRecord
    list_display = ['employee', 'hours', 'reason']
    search_fields = ['employee']

admin.site.register(OvertimeRecord, OvertimeRecordAdmin)

