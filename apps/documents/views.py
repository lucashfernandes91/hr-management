from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Documents

class DocumentCreate(CreateView):
	model = Documents
	fields = ['document_type', 'description', 'file']

	# def form_valid(self, form):
	# 	user = self.request.POST['name'].lower().replace(' ', '_')
	# 	documen = form.save(commit=False)
	# 	employee.enterprise = self.request.user.employee.enterprise
	# 	employee.user = User.objects.create(username=user)
	# 	employee.save()
	# 	messages.success(self.request, "{} criado com sucesso!".format(employee.user))
	# 	return super(EmployeeCreate, self).form_valid(form)
