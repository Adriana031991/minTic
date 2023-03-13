from rest_framework import serializers
from appTienda.models.producto import Producto

class ProductoUpdateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Producto
    fields = ['unidad_medida','unidades_disponibles','precio']

    """def update(self, instance, validated_data):
      instance.unidad_medida = validated_data.get('unidad_medida', instance.unidad_medida)
      instance.unidades_disponibles = validated_data.get('unidades_disponibles', instance.unidades_disponibles)
      instance.precio = validated_data.get('precio', instance.precio)
      instance.save()
      return instance"""

