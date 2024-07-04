from django.urls import path
from .views import UsuarioCreate

urlpatterns = [
    path('register/', UsuarioCreate.as_view(), name='usuario-register'),
]
