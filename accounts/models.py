from django.contrib.auth.models import AbstractUser
from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=52)


class Disease(models.Model):
    name = models.CharField(max_length=52)
    tags = models.ManyToManyField(Tags)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(max_length=52, null=False, blank=False)
    disease = models.ManyToManyField(Disease)
