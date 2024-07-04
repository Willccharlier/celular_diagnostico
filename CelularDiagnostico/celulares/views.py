from rest_framework import generics
from .models import Marca, Modelo
from .serializers import MarcaSerializer, ModeloSerializer

class MarcaList(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ModeloList(generics.ListCreateAPIView):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        marca_id = self.request.query_params.get('marca_id')
        if marca_id:
            queryset = queryset.filter(marca_id=marca_id)
        return queryset
