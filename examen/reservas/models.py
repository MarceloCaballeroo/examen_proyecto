from django.db import models
from django.contrib.auth.models import User

class Reserva(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    vehiculo = models.CharField(max_length=100)
    tipo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.vehiculo}"
