from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.conf import settings

# Create your models here.
class Editor(models.Model):
    editor_name=models.CharField(max_length=100)
    editor_surname=models.CharField(max_length=100)

    def __str__(self):
        return self.editor_name+" "+self.editor_surname

class Client(models.Model):
    client_username=models.CharField(max_length=100)
    client_name=models.CharField(max_length=100)
    client_surname=models.CharField(max_length=100)
    client_pet=models.CharField(max_length=100)
    client_telephone=models.CharField(max_length=20)
    client_email=models.EmailField()
    client_password=models.CharField(max_length=100)

class Package(models.Model):
    package_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    pet=models.CharField(max_length=100)

class Comments(models.Model):
    comments_text = models.TextField()
    comments_editor=models.TextField()
    comments_doctor=models.TextField()
    rating=models.IntegerField()

    def __str__(self):
        return self.comments_text