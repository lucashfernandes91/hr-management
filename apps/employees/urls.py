from django.urls import path
from .views import EmployeeList, EmployeeUpdate, EmployeeDelete, EmployeeCreate


urlpatterns = [
	path('create/', EmployeeCreate.as_view(), name='employee_create'),
	path('', EmployeeList.as_view(), name='employee_list'),
	path('update/<int:pk>/', EmployeeUpdate.as_view(), name='employee_update'),
	path('delete/<int:pk>/', EmployeeDelete.as_view(), name='employee_delete'),
]