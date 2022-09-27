from django.db import models
from .paciente import Pacientes

class Familiar(models.Model):
        documento = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length = 300)
        correo = models.CharField(max_length = 60)
        telefono = models.IntegerField(default=0)
        documento_paciente = models.ForeignKey(Pacientes, related_name='familiar', on_delete=models.CASCADE)