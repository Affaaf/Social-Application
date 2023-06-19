from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    username = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=50, null=True)
    holiday_info = models.CharField(max_length=250, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
