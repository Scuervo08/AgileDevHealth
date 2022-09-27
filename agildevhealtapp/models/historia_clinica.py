from django.db import models
from .medicos import Medicos
from .paciente import Pacientes

class Historia_clinica(models.Model):
    id_historia_clinica= models.BigAutoField(primary_key=True)
    documento_paciente= models.ForeignKey(Pacientes, related_name='historiaclinica', on_delete=models.CASCADE)
    fecha= models.DateTimeField(max_length=30)
    histroia_clinica= models.CharField(max_length=300)
    documento_medico= models.ForeignKey(Medicos, related_name='historiaclinica', on_delete=models.CASCADE)
    diagnostico= models.CharField(max_length=300)
    sugerencias= models.CharField(max_length=300)
