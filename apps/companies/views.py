from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Enterprise


class EnterpriseCreate(CreateView):
	model = Enterprise
	fields = ['name']

	def form_valid(self, form):
		object = form.save()
		employee = self.request.user.employee
		employee.enterprise = object
		employee.save()
		return HttpResponse('OK')
	

class EnterpriseUpdate(UpdateView):
	model = Enterprise
	fields = ['name']
