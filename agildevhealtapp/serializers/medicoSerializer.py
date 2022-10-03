from string import printable
from rest_framework import serializers
from agildevhealtapp.models.medicos import Medicos

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = ['documento_medico', 'nombre', 'apellidos', 'no_tarjetaprof','especialidad']