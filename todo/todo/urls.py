from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from project.views import ProjectModelViewSet, TodoModelViewSet, TodoDetailModelView
from users.views import CustomUserModelViewSet

router = DefaultRouter()
router.register('users', CustomUserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/todo/<int:pk>', TodoDetailModelView.as_view()),
    path('api-token-auth/', views.obtain_auth_token)
]
