from django.db import models

class auxiliar(models.Model):
    documento_auxiliar= models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=30)
    apellidos= models.CharField(max_length=30)
    no_tarjetaprof = models.IntegerField(default=0)
    turno = models.IntegerField(default=0)