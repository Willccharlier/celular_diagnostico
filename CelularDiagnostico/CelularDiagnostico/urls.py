from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/celulares/', include('celulares.urls')),
    path('api/diagnostico/', include('diagnostico.urls')),
]
