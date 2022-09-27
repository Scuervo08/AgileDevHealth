from pyexpat import model
from django.db import models
from .medicos import Medicos
from .paciente import Pacientes

class Registro_signosvitales(models.Model):
    id = models.BigAutoField(primary_key=True)
    documento_paciente=models.ForeignKey(Pacientes,related_name='Rsignosvitales',on_delete=models.CASCADE)
    documento_medico =models.ForeignKey(Medicos,related_name='Rsignosvitales',on_delete=models.CASCADE)
    fecha_ingreso =models.DateTimeField()