from distutils.command.upload import upload
from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    photo = models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now_add=True)