from tienda import settings

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from appTienda.models.user import User
from appTienda.serializers.userSerializer import UserSerializer
from appTienda.serializers.userUpdateSerializer import UserUpdateSerializer


class UserDetailView(views.APIView):
  users = User.objects.all()
  
  def get(self, request, *args, **kwargs):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token, verify=False)
    
    # if (valid_data['user_id'] != kwargs['pk']):
    #   error = { 'message': 'Credenciales inválidas!' }
    #   return Response(error, status=status.HTTP_401_UNAUTHORIZED)
    
    # user = self.users.get(id=kwargs['pk'])
    user = self.users.get(id=valid_data['user_id'])
    user_serializer = UserSerializer(user)

    return Response(user_serializer.data, status=status.HTTP_200_OK)

  def put(self, request, *args, **kwargs):
    user = self.productos.filter(id = kwargs['pk']).first()
    if(user):
      user_serializer = UserUpdateSerializer(user, data = request.data)

      if(user_serializer.is_valid(raise_exception = True)):
          user_serializer.save
          return Response({'message': 'Usuario actualizado'}, status = status.HTTP_200_OK)

      return Response({'message': 'Detalles no válidos'}, status = status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'Usuario no encontrado'}, status = status.HTTP_404_NOT_FOUND)
