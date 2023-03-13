from django.conf import settings
from rest_framework import generics,  status, views
from rest_framework.response import Response
from appTienda.models.producto import Producto
from appTienda.serializers.productoSerializer import ProductoSerializer

class ProductoView(generics.ListAPIView):

    queryset           = Producto.objects.all()
    serializer_class   = ProductoSerializer
    def get_queryset(self):
        return super().get_queryset()