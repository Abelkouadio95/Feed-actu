from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Messages(models.Model):
    content = models.CharField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Phrases(models.Model):
    Ph = models.CharField(max_length=280)