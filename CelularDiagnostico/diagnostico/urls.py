from django.urls import path
from .views import DiagnosticoCreate, ReparoCreate

urlpatterns = [
    path('diagnostico/', DiagnosticoCreate.as_view(), name='diagnostico-create'),
    path('reparo/', ReparoCreate.as_view(), name='reparo-create'),
]
