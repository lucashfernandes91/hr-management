from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.employees.models import Employee


@login_required
def home(request):
	data = {}
	data['user'] = request.user
	return render(request, 'core/index.html', data)
