from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Employee
from django.contrib.auth.models import User


class EmployeeCreate(CreateView):
	model = Employee
	fields = ['name', 'departments', 'email', 'phone']

	def form_valid(self, form):
		user = self.request.POST['name'].lower().replace(' ', '_')
		employee = form.save(commit=False)
		employee.enterprise = self.request.user.employee.enterprise
		employee.user = User.objects.create(username=user)
		employee.save()
		return super(EmployeeCreate, self).form_valid(form)


class EmployeeList(ListView):
	model = Employee
	paginate_by = 10

	
	def get_queryset(self):
		employee_looged = self.request.user.employee.enterprise
		return Employee.objects.filter(enterprise=employee_looged)
	

class EmployeeUpdate(UpdateView):
	model = Employee
	fields = ['name', 'email', 'phone']


class EmployeeDelete(DeleteView):
	model = Employee
	success_url = reverse_lazy('employee_list')