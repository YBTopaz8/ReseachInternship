from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("Username"), max_length=50, default="Def")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
class Invit(models.Model):
     invCode = models.CharField('Invitation Code', max_length=50)   
     dateCreated = models.DateTimeField( auto_now=True)
     quantity = models.IntegerField(default=1)
     def __str__(self):
        return "{} ".format(self.invCode,self.quantity) 

     class Meta:
        verbose_name = 'Invitation Code'
        verbose_name_plural = 'Invitation Codes'