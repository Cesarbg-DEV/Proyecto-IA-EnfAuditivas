from django.db import models

# Create your models here.
class Enfermedades(models.Model):
    nombre = models.CharField(max_length=50)
    fiebre = models.FloatField(max_length=5)
    perdAuditiva= models.FloatField(max_length=5)
    dolorOido = models.FloatField(max_length=5)
    inflamacion = models.FloatField(max_length=5)
    mareo = models.FloatField(max_length=5)
    vertigo = models.FloatField(max_length=5)
    enrojecimiento = models.FloatField(max_length=5)
    fatiga = models.FloatField(max_length=5)
    difComunicacion = models.FloatField(max_length=5)
    zumbidos = models.FloatField(max_length=5)
    taponamiento = models.FloatField(max_length=5)
    antecedentes = models.FloatField(max_length=5)
    picazon = models.FloatField(max_length=5)
    traumas = models.FloatField(max_length=5)
    sangrado = models.FloatField(max_length=5)
    sumaEnfermedad = models.FloatField(default=0)


