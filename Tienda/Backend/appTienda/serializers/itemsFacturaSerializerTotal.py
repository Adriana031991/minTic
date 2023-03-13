from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models.itemsFactura import ItemsFactura
from ..models.producto import Producto

class ItemsFacturaSerializerTotal(serializers.ModelSerializer):
    class Meta:
        model   = ItemsFactura
        fields= '__all__'
    def to_representation(self, instance):
        item=ItemsFactura.objects.get(id=instance.id)
        return item
        

