from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, SlugRelatedField

from users.serialiazers import CustomUserModelSerializer
from .models import Project, TODO


class ProjectModelSerializer(ModelSerializer):

    # user = CustomUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    # project = SlugRelatedField(slug_field="name_project", read_only=True)
    # user = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = TODO
        fields = '__all__'
