from pyexpat import model
from django.db import models
from agildevhealtapp.models import medicos
from models import paciente
from .user import User

class registro_signosvitales(models.Model):
    id = models.BigAutoField(primary_key=True)
    documento_paciente=models.ForeignKey(paciente,related_name='documento_paciente',on_delete=models.CASCADE)
    documento_medico =models.ForeignKey(medicos,related_name='documento_medico',on_delete=models.CASCADE)
    fecha_ingreso =models.DateTimeField()