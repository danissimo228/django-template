from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    """
    Django command class for creating an administrator for the admin panel
    """
    help = "Creating administrator"

    def handle(self, *args, **options) -> None:
        if not User.objects.filter(username=settings.ADMIN_USERNAME).exists():
            User.objects.create_superuser(
                username=settings.ADMIN_USERNAME,
                password=settings.ADMIN_PASSWORD,
                email=settings.ADMIN_EMAIL,
            )
            self.stdout.write("Administrator creation was successful.")
        else:
            self.stdout.write("Administrator already exists.")
