from django.core.management import BaseCommand
from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.com',
            telegram='admin',
            phone='88005553535',
            first_name='Админ',
            last_name='Админов',
            birthday='1990-01-01',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('admin')
        user.save()
