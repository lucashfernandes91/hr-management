from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.overtime_record.forms import OvertimeRecordForm
from .models import OvertimeRecord


class OvertimeRecordList(ListView):
	model = OvertimeRecord

	def get_queryset(self):
		employee_looged = self.request.user.employee
		return OvertimeRecord.objects.filter(employee=employee_looged)
		#return OvertimeRecord.objects.filter(employee__enterprise=employee_looged)

class OvertimeRecordUpdate(UpdateView):
	model = OvertimeRecord
	form_class = OvertimeRecordForm

	def get_form_kwargs(self):
		kwargs = super(OvertimeRecordUpdate, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs

class OvertimeRecordDelete(DeleteView):
	model = OvertimeRecord	
	success_url = reverse_lazy('overtime_record_list')

class OvertimeRecordCreate(CreateView):
	model = OvertimeRecord
	form_class = OvertimeRecordForm

	def get_form_kwargs(self):
		kwargs = super(OvertimeRecordCreate, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs