from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Project, TODO
from .serialiazers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, TodoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilter


class TodoDetailModelView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, pk):
        todo = TODO.objects.get(id=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(TODO.objects.all(), pk=pk)
        todo.status_todo = True
        todo.save()
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = TODO.objects.get(id=pk)
        serializer = TodoModelSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
