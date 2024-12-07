from django.forms import ModelForm
from .models import OvertimeRecord
from apps.employees.models import Employee


class OvertimeRecordForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(OvertimeRecordForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(
            enterprise=user.employee.enterprise)

    class Meta:
        model = OvertimeRecord
        fields = ['reason', 'employee', 'hours']