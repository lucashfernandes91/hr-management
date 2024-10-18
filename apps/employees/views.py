from django.http import HttpResponse
from django.views.generic import ListView
from .models import Employee


class EmployeeList(ListView):
	model = Employee
	paginate_by = 10