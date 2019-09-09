from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User



class MyAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must required an email")

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password = password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email =             models.EmailField(verbose_name='email', max_length=60, unique=True)
    username =          models.CharField(max_length=30, unique=True, null=True, blank=True)
    date_joined =       models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login =        models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin =          models.BooleanField(default=False)
    is_active =         models.BooleanField(default=True)
    is_staff =          models.BooleanField(default=False)
    is_superuser =      models.BooleanField(default=False)

    USERNAME_FIELD =    'email'

    objects =           MyAccountManager()

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
