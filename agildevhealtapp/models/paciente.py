from django.db import models
from agildevhealtapp.models.auxiliar import auxiliar
from agildevhealtapp.models.medicos import medico
from models import enfermero

class paciente(models.Model):
    nombre= models.CharField(max_length=30)
    direccion= models.CharField(max_length=30)
    apellidos= models.CharField(max_length=30)
    telefono= models.IntegerField(default=0)
    documento_paciente=models.IntegerField(primary_key=True)
    documento_auxiliar= models.ForeignKey(auxiliar, related_name='documento_auxiliar', on_delete=models.CASCADE)
    documento_enfermero= models.ForeignKey(enfermero, related_name='documento_enfermero', on_delete=models.CASCADE)
    documento_medico =models.ForeignKey(medico, related_name='documento_medico', on_delete=models.CASCADE)
    fecha_ingreso =models.DateTimeField()