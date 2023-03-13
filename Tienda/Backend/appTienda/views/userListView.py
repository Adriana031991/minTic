from rest_framework                            import status, views, generics
from rest_framework.response                   import Response
from rest_framework_simplejwt.serializers      import TokenObtainPairSerializer

from appTienda.models import User
from appTienda.serializers.userSerializer import UserSerializer


class UserListView(generics.ListAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def get_queryset(self):
        return super().get_queryset()