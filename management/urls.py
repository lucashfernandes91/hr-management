from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', include('apps.core.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
	path('funcionarios/', include('apps.employees.urls')),
	path('empresa/', include('apps.companies.urls')),
	path('colaboradores/', include('apps.departments.urls')),
	path('documentos/', include('apps.documents.urls')),
	path('hora-extra/', include('apps.overtime_record.urls')),
	path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)