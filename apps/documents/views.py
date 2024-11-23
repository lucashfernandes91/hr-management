from .models import Documents
from django.views.generic import CreateView


class DocumentCreate(CreateView):
    model = Documents
    fields = ['description', 'document_type', 'file']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.employee_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)