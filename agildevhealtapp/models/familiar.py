from django.db import models
from models import paciente

class familiar(models.Model):
        documento = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length = 300)
        correo = models.CharField(max_length = 60)
        telefono = models.IntegerField(default=0)
        documento_paciente = models.ForeignKey(paciente, related_name='documento_paciente', on_delete=models.CASCADE)