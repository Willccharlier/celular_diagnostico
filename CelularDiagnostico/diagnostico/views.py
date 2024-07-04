from rest_framework import generics
from .models import Diagnostico, Reparo
from .serializers import DiagnosticoSerializer, ReparoSerializer

class DiagnosticoCreate(generics.CreateAPIView):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer

class ReparoCreate(generics.ListCreateAPIView):
    queryset = Reparo.objects.all()
    serializer_class = ReparoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        diagnostico_id = self.request.query_params.get('diagnostico_id')
        if diagnostico_id:
            queryset = queryset.filter(diagnostico_id=diagnostico_id)
        return queryset
