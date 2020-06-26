from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthdate = models.DateField('Data de Nascimento', blank = True, null = True)
    phone = models.CharField('Nr. Telefone', max_length=20, blank = True, null = True)

   