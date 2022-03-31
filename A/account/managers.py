from django.contrib.auth.models import BaseUserManager

"""
  Customizing Manager of User for Change Auth Field to Phone Number for Default Username
"""


class UserManagers(BaseUserManager):
    def create_user(self, email, phone, full_name, password=None):
        """
                Creates and saves a User with the given email, phone number,
                 full name and password.
                """
        if not email:
            raise ValueError('Users must have an email address')
        if not phone:
            raise ValueError('Users must have a phone number')
        if not full_name:
            raise ValueError('Users must have a full name')

        user = self.model(email=self.normalize_email(email), phone=phone, full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, phone, full_name, password=None):

        """
           Creates and saves a superuser with the given email, phone number,
           full name and password.
         """
        user = self.create_user(email, phone, full_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
