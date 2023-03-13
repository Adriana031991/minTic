from rest_framework import status, views
from rest_framework.response import Response
from appTienda.serializers.userSerializer import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserCreateView(views.APIView):
  def post(self, request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    print(serializer.validated_data)
    
    token_data = {
      'username': request.data['username'],
      'password': request.data['password'],
    }
    token_serializer = TokenObtainPairSerializer(data=token_data)
    token_serializer.is_valid(raise_exception=True)

    return Response(token_serializer.validated_data, status=status.HTTP_200_OK)