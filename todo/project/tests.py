from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer

from users.models import CustomUser
from .views import ProjectModelViewSet
from .models import Project


class TestProjectModelViewSet(TestCase):

    def setUp(self):
        self.url = '/api/project/'
        self.url_user = '/api/users/'
        self.url2 = '/api/todo/'

        self.email = 'admin2@admin.ru'
        self.password = '12345'
        self.admin = CustomUser.objects.create_superuser('admin2', self.email, self.password)

        self.data_project = {
            'name_project': 'Project 5',
            'url_project': 'https://project-5.ru',
            'users': [1]
        }
        self.data_project_m2m = {
            'name_project': 'Project 5',
            'url_project': 'https://project-5.ru',
        }

        self.data_project_m2m_2 = {
            'name_project': 'Project 52',
            'url_project': 'https://project-52.ru',
            'users': [1]
        }

        self.data_user = {
            "username": "user4",
            "first_name": "Андрей",
            "last_name": "Смирнов",
            "email": "user4@user.ru"
        }

        self.data_user2 = {
            "username": "user42",
            "first_name": "Андрей2",
            "last_name": "Смирнов2",
            "email": "user42@user.ru"
        }

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creat_quest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data_project, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creat_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.data_project, format='json')
        force_authenticate(request, user=self.admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        client = APIClient()
        project = Project.objects.create(**self.data_project_m2m)
        project.users.add(CustomUser.objects.get(id=1))
        response = client.get(f'{self.url}{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_user(self):
        client = APIClient()
        user = CustomUser.objects.create(**self.data_user)
        response = client.get(f'{self.url_user}{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_guest(self):
        client = APIClient()
        project = Project.objects.create(**self.data_project_m2m)
        project.users.add(CustomUser.objects.get(id=1))
        response = client.put(f'{self.url}{project.id}/', self.data_project)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin(self):
        client = APIClient()
        user = CustomUser.objects.create(**self.data_user)

        client.login(email=self.email, password=self.password)

        response = client.put(f'{self.url_user}{user.id}/', self.data_user2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_update = CustomUser.objects.get(id=user.id)

        self.assertEqual(user_update.username, 'user42')
        self.assertEqual(user_update.first_name, 'Андрей2')
        self.assertEqual(user_update.last_name, 'Смирнов2')
        self.assertEqual(user_update.email, 'user42@user.ru')

        client.logout()

    def test_get_admin2(self):
        client = APIClient()
        project = Project.objects.create(**self.data_project_m2m)
        project.users.add(CustomUser.objects.get(id=1))

        client.login(email=self.email, password=self.password)

        response = client.put(f'{self.url}{project.id}/', self.data_project_m2m_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project_update = Project.objects.get(id=project.id)

        self.assertEqual(project_update.name_project, 'Project 52')
        self.assertEqual(project_update.url_project, 'https://project-52.ru')

        client.logout()

    def tearDown(self) -> None:
        pass


class APITestCaseProjectViewSet(APITestCase):

    def setUp(self):
        self.url_project = '/api/project/'
        self.url_user = '/api/users/'
        self.url_todo = '/api/todo/'

        self.email = 'admin2@admin.ru'
        self.password = '12345'
        self.admin = CustomUser.objects.create_superuser('admin2', self.email, self.password)

        self.data_project = {
            'name_project': 'Project 5',
            'url_project': 'https://project-5.ru',
            'users': [1]
        }
        self.data_project_m2m = {
            'name_project': 'Project 5',
            'url_project': 'https://project-5.ru',
        }

        self.data_user = {
            "username": "user4",
            "first_name": "Андрей",
            "last_name": "Смирнов",
            "email": "user4@user.ru"
        }

        self.data_user2 = {
            "username": "user42",
            "first_name": "Андрей2",
            "last_name": "Смирнов2",
            "email": "user42@user.ru"
        }

    def test_get_list(self):
        response = self.client.get(self.url_project)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = CustomUser.objects.create(**self.data_user)
        project = Project.objects.create(**self.data_project_m2m)
        project.users.add(user.id)
        self.client.login(email=self.email, password=self.password)
        response = self.client.put(f'{self.url_project}{project.id}/', {'name_project': 'Project 52',
                                                                        'url_project': 'https://project-52.ru',
                                                                        'users': user.id
                                                                        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project_update = Project.objects.get(id=project.id)
        self.assertEqual(project_update.name_project, 'Project 52')
        self.client.logout()

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        self.client.login(email=self.email, password=self.password)
        response = self.client.put(f'{self.url_project}{project.id}/', {'name_project': 'Project 52',
                                                                        'url_project': 'https://project-52.ru',
                                                                        'users': [1]
                                                                        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project_update = Project.objects.get(id=project.id)
        self.assertEqual(project_update.name_project, 'Project 52')
        self.client.logout()



class TestMath(APISimpleTestCase):

    def Test_sqrt(self):
        import math
        response = math.sqrt(4)
        self.assertEqual(response, 2)