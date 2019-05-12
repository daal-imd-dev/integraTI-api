from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(AbstractUser, BaseModel):
    sigaa_registration_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    sigaa_user_name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    sigaa_token = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
