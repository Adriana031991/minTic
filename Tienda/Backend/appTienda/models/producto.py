from django.db import models
class Producto(models.Model):
    id  = models.AutoField(primary_key=True)
    ref=models.CharField(max_length=25, null=False)
    nombre=models.CharField(max_length=45, null=False)
    categoria=models.CharField(max_length=35,  null=False)
    marca=models.CharField(max_length=25)
    unidad_medida=models.CharField(max_length=45)
    unidades_disponibles=models.IntegerField()
    precio=models.FloatField()