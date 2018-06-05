from rest_framework import serializers
from drogeria.models import Paciente, Medicamento, Sede

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sede
        fields=('id','nombre')

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicamento
        fields=('id','nombre','foto')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paciente
        fields=('identificacion','nombres','apellidos','receta','medicamento_id','sede_id')