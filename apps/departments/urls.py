from django.urls import path
from .views import DepartmentCreate, DepartmentUpdate, DepartmentList, DepartmentDelete


urlpatterns = [
	path('create/', DepartmentCreate.as_view(), name='department_create'),
	path('', DepartmentList.as_view(), name='department_list'),	
	path('update/<int:pk>/', DepartmentUpdate.as_view(), name='department_update'),
	path('delete/<int:pk>/', DepartmentDelete.as_view(), name='department_delete')
]