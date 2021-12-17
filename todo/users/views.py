from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import CustomUser
from .serialiazers import CustomUserModelSerializer, CustomUserModelSerializerV2
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin


# class UserLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10


class CustomUserModelViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    # serializer_class = CustomUserModelSerializer
    # pagination_class = UserLimitOffsetPagination

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return CustomUserModelSerializerV2
        return CustomUserModelSerializer


# class CustomUserModelListAPIView(ListAPIView):
#     queryset = CustomUser.objects.all()
#
#     def get_serializer_class(self):
#         if self.request.version == 'v2':
#             return CustomUserModelSerializerV2
#         return CustomUserModelSerializer
