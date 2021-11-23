from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from users.serialiazers import CustomUserModelSerializer
from .models import Project, TODO


class ProjectModelSerializer(ModelSerializer):

    # user = CustomUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        fields = '__all__'
