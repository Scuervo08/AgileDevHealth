from django.db import models
from .auxiliar import Auxiliar
from .medicos import Medicos
from .enfermero import Enfermero

class Pacientes(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    apellidos= models.CharField(max_length=30)
    telefono= models.IntegerField(default=0)
    documento_paciente=models.IntegerField(primary_key=True)
    documento_auxiliar= models.ForeignKey(Auxiliar, related_name='paciente', on_delete=models.CASCADE)
    documento_enfermero= models.ForeignKey(Enfermero, related_name='paciente', on_delete=models.CASCADE)
    documento_medico =models.ForeignKey(Medicos, related_name='paciente', on_delete=models.CASCADE)
    fecha_ingreso =models.DateTimeField()