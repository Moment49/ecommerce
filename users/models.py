from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, username=None):
        if email is None:
            return ValidationError("Email must not be empty")
        if password is None:
            return ValidationError("Password must not be empty")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create a custom Use model
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=False, null=True)
    email = models.CharField(max_length=100, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
