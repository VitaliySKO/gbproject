from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from graphene_django.views import GraphQLView

from project.views import ProjectModelViewSet, TodoModelViewSet, TodoDetailModelView
from users.views import CustomUserModelViewSet

router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title='ToDo',
        default_version='v2',
        description='Documentation',
        contact=openapi.Contact(email='todo@todo.ru'),
        license=openapi.License(name='Todo')
    ),
    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/todo/<int:pk>', TodoDetailModelView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger')),
    path('swagger/<str:format>/', schema_view.without_ui()),
    path('redoc/', schema_view.with_ui('redoc')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
