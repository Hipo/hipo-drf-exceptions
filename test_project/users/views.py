from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class RegistrationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
