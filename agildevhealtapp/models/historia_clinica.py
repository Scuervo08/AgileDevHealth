from django.db import models
from models import medicos
from models import paciente

class historia_clinica(models.Model):
    id_historia_clinica= models.BigAutoField(primary_key=True)
    documento_paciente= models.ForeignKey(paciente, related_name='documento_paciente', on_delete=models.CASCADE)
    fecha= models.DateTimeField(max_length=30)
    histroia_clinica= models.CharField(max_length=300)
    documento_medico= models.ForeignKey(medicos, related_name='documento_medico', on_delete=models.CASCADE)
    diagnostico= models.CharField(max_length=300)
    sugerencias= models.CharField(max_length=300)
