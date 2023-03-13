from django.db import models
class Factura(models.Model):
    id  = models.AutoField(primary_key=True)
    fecha=models.DateField(auto_now_add=True)
    tipo_doc=models.CharField("Tipo de documento",help_text="Tipo de documento", max_length=2, null=False)
    num_doc=models.CharField("Numero de documento", help_text="Numero de documento", max_length=12, null=False)
    nombres=models.CharField("Nombres del cliente", help_text="Nombres del cliente", max_length=25, null=False)
    apellidos=models.CharField("Apellidos del cliente", max_length=25, null=False)
    total_items=models.IntegerField()
    total_factura=models.FloatField()