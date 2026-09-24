import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Create or update the production Django superuser."

    def handle(self, *args, **options):

        User = get_user_model()

        username = os.getenv("ADMIN_USERNAME")
        email = os.getenv("ADMIN_EMAIL", "")
        password = os.getenv("ADMIN_PASSWORD")

        if not username or not password:
            self.stderr.write(
                "ADMIN_USERNAME and ADMIN_PASSWORD must be set."
            )
            return

        user = User.objects.filter(
            username=username
        ).first()

        if user is None:

            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser '{username}' created successfully."
                )
            )

        else:

            user.email = email
            user.set_password(password)
            user.is_staff = True
            user.is_superuser = True
            user.is_active = True

            user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f"Superuser '{username}' updated successfully."
                )
            )