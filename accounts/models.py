from django.contrib.auth.models import AbstractUser
from django.db import models


class Tags(models.Model):
    name = models.CharField()


class Disease(models.Model):
    name = models.CharField()
    tags = models.ManyToManyField(Tags)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(null=False, blank=False)
    disease = models.ManyToManyField(Disease)
