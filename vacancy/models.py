from django.db import models
from django import forms
import django

# Create your models here.


class Vacancy(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)
