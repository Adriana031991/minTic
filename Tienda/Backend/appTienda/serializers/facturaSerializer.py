from django.db import models
from django.db.models import fields
from rest_framework import serializers
from appTienda.models.producto import Producto
from appTienda.serializers import itemsFacturaSerializer
from appTienda.serializers.itemsFacturaSerializer import ItemsFacturaSerializer
from appTienda.serializers.itemsFacturaSerializerTotal import ItemsFacturaSerializerTotal
from ..models.itemsFactura import ItemsFactura
from ..models.factura import Factura


class FacturaSerializer(serializers.ModelSerializer):
    itemsfactura=ItemsFacturaSerializer(many=True)
    class Meta:
        model   = Factura
        fields = ['tipo_doc','num_doc', 'nombres','apellidos','itemsfactura']
    def create(self, validated_data):
        itemsData=validated_data.pop('itemsfactura')
        items_de_factura=0
        suma=0
        for i in itemsData:
            items_de_factura+=i['unidades']
            dato=Producto.objects.filter(id=i['idProducto'].id).values('precio').first()
            dato['precio']
            suma+=(i['unidades']*dato['precio'])
      
        facturaInstance=Factura.objects.create(**validated_data,total_items=items_de_factura , total_factura=suma)
        
        for i in itemsData:   
            dato=Producto.objects.filter(id=i['idProducto'].id).values('precio','unidades_disponibles').first()
            ItemsFactura.objects.create(idFactura=facturaInstance,**i,precio=dato['precio'],subtotal=i['unidades']*dato['precio'])
            actualizar=Producto.objects.filter(id=i['idProducto'].id).first()
            actualizar.unidades_disponibles-=i['unidades']
            actualizar.save()
            
        return facturaInstance
    
    def to_representation(self, instance):
        factura=Factura.objects.get(id=instance.id)
        item=ItemsFactura.objects.filter(idFactura=instance.id)
        lista=[]
        for i in ItemsFacturaSerializerTotal(item, many=True).data:
            x={
                'idItem': i.id,
                'id': i.idProducto.id,
                'ref':i.idProducto.ref,
                'nombre':i.idProducto.nombre,
                'categoria':i.idProducto.categoria,
                'marca':i.idProducto.marca,
                'unidad_medida':i.idProducto.unidad_medida,
                'unidades':i.unidades,
                'precio':i.precio,
                'subtotal':i.subtotal
            }
            lista.append(x)
        return {
            "id":factura.id,    
            "fecha":factura.fecha,        
            "tipo_doc":factura.tipo_doc,
            "num_doc":factura.num_doc,
            "nombres":factura.nombres,
            "apellidos":factura.apellidos,
            "total_items":factura.total_items,
            "total_factura":factura.total_factura,
            "itemsFactura": lista

            }
