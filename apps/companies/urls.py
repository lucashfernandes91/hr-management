from django.urls import path

from .views import EnterpriseCreate, EnterpriseUpdate


urlpatterns = [
	path('create', EnterpriseCreate.as_view(), name='create_company'),
	path('update/<int:pk>/', EnterpriseUpdate.as_view(), name='update_company'),
]
