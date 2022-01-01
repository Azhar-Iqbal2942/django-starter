from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin

# Custom Imports
from core.managers import AccountManager



class Account(AbstractBaseUser, PermissionsMixin):
    """Custom User models that support email instead of username"""
    first_name = models.CharField(verbose_name='first name', max_length=20)
    last_name  = models.CharField(verbose_name='last name', max_length=20)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = AccountManager()

    def __str__(self):
        return self.email
