from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        user.objects.create_superuser(username='admin', email='admin@admin.ru', password='12345')
        print('superuser - создан\n    login:admin@admin.ru\n    password:12345')
        for i in range(1, 4):
            user.objects.create_user(username=f'user{i}', email=f'user{i}@user.ru', password='12345')
            print(f'user{i} - создан')