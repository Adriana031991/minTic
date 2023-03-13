from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models.itemsFactura import ItemsFactura
from ..models.producto import Producto

class ItemsFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model   = ItemsFactura
        fields  = ['idProducto','unidades']

