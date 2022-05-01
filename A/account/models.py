from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.managers import UserManagers


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """
    Customization User Model for Change Default User Name to Phone Number for Auth Pages
    """
    email = models.EmailField(max_length=250, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManagers()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class OtPCode(models.Model):
    phone = models.CharField(max_length=11, unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone}-{self.code}-{self.created}"