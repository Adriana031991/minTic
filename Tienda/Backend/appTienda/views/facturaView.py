
from rest_framework import generics, status, views
from rest_framework import permissions
from rest_framework.response import Response
#from Backend.tienda import settings
from appTienda.models.factura import Factura
from appTienda.serializers.facturaSerializer import FacturaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from tienda import settings
from datetime import date

class CreateFacturaView(views.APIView):
    #permission_classes = (IsAuthenticated)
    def post(self, request, *args, **kwargs):   
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        serializer=FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FacturaListView(generics.ListAPIView):
    queryset           = Factura.objects.filter(fecha=date.today())
    serializer_class   = FacturaSerializer
    #permission_classes = (IsAuthenticated)

    def get_queryset(self):
        """token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)"""
        return  super().get_queryset()

class FacturaDetailView(generics.RetrieveAPIView):
    queryset           = Factura.objects.all()
    serializer_class   = FacturaSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False) 
        #valid_data.is_valid()    
        return super().get( request, *args, **kwargs)


