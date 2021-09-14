from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass
	

class Available_user_pokemon(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)


