from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    description = models.TextField()
    upload = models.ImageField(upload_to='image/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)