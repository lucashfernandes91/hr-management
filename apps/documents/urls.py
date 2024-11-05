from django.urls import path
from .views import DocumentCreate #, DepartmentUpdate, DepartmentList, DepartmentDelete


urlpatterns = [
	path('create/', DocumentCreate.as_view(), name='document_create'),
	# path('', DepartmentList.as_view(), name='department_list'),	
	# path('update/<int:pk>/', DepartmentUpdate.as_view(), name='department_update'),
	# path('delete/<int:pk>/', DepartmentDelete.as_view(), name='department_delete')
]