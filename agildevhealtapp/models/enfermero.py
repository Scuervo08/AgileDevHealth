from django.db import models

class Enfermero(models.Model):
        documento_enfermero = models.IntegerField(primary_key=True)
        primer_nombre = models.CharField(max_length = 30)
        segundo_nombre = models.CharField(max_length = 30)
        primer_apellido = models.CharField(max_length = 30)
        segundo_apellido = models.CharField(max_length = 30)
        turno = models.IntegerField(default=0)
        area_trabajo = models.CharField(max_length = 300)