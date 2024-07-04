from django.urls import path
from .views import MarcaList, ModeloList

urlpatterns = [
    path('marcas/', MarcaList.as_view(), name='marca-list'),
    path('modelos/', ModeloList.as_view(), name='modelo-list'),
]
