from users.models import Profile
from django.urls import reverse
from django.db import models
# Create your models here.


class Post(models.Model):
    image = models.ImageField(upload_to="blog/photos",
                              blank=True, null=True)
    image_center = models.ImageField(
        upload_to="blog/photos", blank=True, null=True)
    image_left = models.ImageField(
        upload_to="blog/photos", blank=True, null=True)
    image_right = models.ImageField(
        upload_to="blog/photos", blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    vip_content = models.BooleanField(default=False)
    category = models.ManyToManyField(
        "Category")
    description = models.CharField(max_length=500, null=True, blank=True)
    github_url = models.CharField(max_length=500, null=True, blank=True)

    class Meta():
        ordering = ['created_at']

    def __ster__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={"pk": self.id})


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
