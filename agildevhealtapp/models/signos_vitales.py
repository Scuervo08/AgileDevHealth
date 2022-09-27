from django.db import models

class Signosvitales(models.Model):
        id = models.BigAutoField(primary_key=True)
        temperatura = models.CharField(max_length=45)
        presion_arterial = models.CharField(max_length = 45)
        oximetriua = models.CharField(max_length = 45)
        frecuencia_cardiaca = models.CharField(max_length = 45)
        glicemias = models.CharField(max_length=45)