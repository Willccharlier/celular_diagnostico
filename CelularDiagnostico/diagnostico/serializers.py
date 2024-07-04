from rest_framework import serializers
from .models import Diagnostico, Reparo

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'

class ReparoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparo
        fields = '__all__'
