from datetime import datetime as dt

import pytz
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
    
    @property
    def since_last_login(self):
        if not self.last_login:
            return '-'
        timediff = (dt.now(pytz.utc) - self.last_login)
        
        days = timediff.days
        if days > 0:
            return f"{days} d."
            
        hours = timediff.seconds // 3600
        if hours < 0:
            return '-'
        return f"{int(hours)} h."
