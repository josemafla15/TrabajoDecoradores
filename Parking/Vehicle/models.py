from django.db import models

class vehicle(models.Model):
    COLOR=(
        ('1','"ROJO'),
        ('2','"AZUL'),
        ('3','"VERDE'),
    )

    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color_vehiculo=models.CharField('color',max_length=1, choices=COLOR)
    modelo=models.IntegerField()