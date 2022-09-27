from django.db import models



class Medicos(models.Model):
    documento_medico= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellidos= models.CharField(max_length=30)
    no_tarjetaprof = models.IntegerField(default=0)
    especialidad = models.CharField(max_length=30)