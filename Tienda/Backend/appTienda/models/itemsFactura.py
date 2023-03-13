from django.db import models
from .producto import Producto
from .factura import Factura
class ItemsFactura(models.Model):
    id  = models.AutoField(primary_key=True)
    idFactura=models.ForeignKey(Factura, related_name='factura', on_delete=models.CASCADE)
    idProducto=models.ForeignKey(Producto, related_name='producto', on_delete=models.CASCADE)
    unidades=models.IntegerField()
    precio=models.FloatField()
    subtotal=models.FloatField()