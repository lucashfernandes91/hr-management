from django.urls import path
from .views import DocumentCreate


urlpatterns = [
	path('create/<int:pk>/', DocumentCreate.as_view(), name='document_create'),
]