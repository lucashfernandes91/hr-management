from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Departments


class DepartmentCreate(CreateView):
	model = Departments
	fields = ['name', 'enterprise', 'email', 'phone']

	def form_valid(self, form):
		department = form.save(commit=False)
		department.name = department.name
		department.enterprise = self.request.user.employee.enterprise
		department.email = department.email
		department.phone = department.phone
		department.save()
		messages.success(self.request, "{} criado com sucesso!".format(department.name))
		return super(DepartmentCreate, self).form_valid(form)

class DepartmentUpdate(UpdateView):
	model = Departments
	fields = ['name', 'enterprise', 'email', 'phone']
	
class DepartmentList(ListView):
	model = Departments
	paginate_by = 10

	def get_queryset(self):
		enterprise_looged = self.request.user.employee.enterprise
		return Departments.objects.filter(enterprise=enterprise_looged)

class DepartmentDelete(DeleteView):
	model = Departments
	success_url = reverse_lazy('department_list')