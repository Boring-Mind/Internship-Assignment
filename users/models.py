from django.contrib.auth.models import AbstractUser, UserManager


class UserManager(UserManager):
    def create(self, *args, **kwargs):
        """Override default create method.

        Create_user method is needed
        for proper password hashing
        and field validation.
        """
        return super().create_user(*args, **kwargs)


class User(AbstractUser):
    objects = UserManager()
