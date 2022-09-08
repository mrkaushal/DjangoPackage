import os
from django.db import models


# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.pk, ext)
    return os.path.join('uploads', filename)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    description = models.TextField()
    image = models.ImageField(upload_to=content_file_name)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        self.image.delete(self.image.name)
        super().delete()
