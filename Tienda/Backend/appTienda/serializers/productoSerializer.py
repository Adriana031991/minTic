from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Producto
        fields  = ['id','ref','nombre','categoria','marca','unidad_medida','unidades_disponibles','precio']

        def create(self, validated_data):
            producto=Producto.objects.create(**validated_data)
            return producto
            
        def to_representation(self, obj):
            producto=Producto.objects.get(id=obj.id)
            return {
                'id':producto.id,
                'ref':producto.ref,
                'nombre':producto.nombre,
                'categoria':producto.categoria,
                'marca':producto.marca,
                'unidad_medida':producto.unidad_medida,
                'unidades_disponibles':producto.unidades_disponibles,
                'precio':producto.precio
            }

