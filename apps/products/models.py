from django.db import models

from apps.products.utils import image_upload_path


class Product(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to=image_upload_path, null=True)
    description = models.TextField()


class Resume(models.Model):
    full_name = models.CharField(max_length=225)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=225)
    text = models.TextField()
    resume = models.FileField()


class Certificate(models.Model):
    image = models.ImageField(upload_to=image_upload_path)