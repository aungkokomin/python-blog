from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    id = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

