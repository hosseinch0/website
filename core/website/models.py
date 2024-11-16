from users.models import CustomUser, Profile
from django.db import models
# Create your models here.


class Contact(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    email = models.EmailField(max_length=300)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class NewsLetter(models.Model):
    sender = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
