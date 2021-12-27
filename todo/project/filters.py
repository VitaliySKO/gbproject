from django_filters import rest_framework as filters
from .models import Project, TODO


class ProjectFilter(filters.FilterSet):
    name_project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name_project']


class TodoFilter(filters.FilterSet):
    # project = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TODO
        fields = ['project']
