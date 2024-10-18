from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path('', include('apps.core.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	path('funcionarios/', include('apps.employees.urls')),
    path('empresa/', include('apps.companies.urls')),
	path('admin/', admin.site.urls),
]
