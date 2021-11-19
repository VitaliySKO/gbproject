from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serialiazers import CustomUserModelSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer