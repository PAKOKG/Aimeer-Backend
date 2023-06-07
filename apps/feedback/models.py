from django.db import models

from apps.feedback.utils import RATE_CHOICE


class Feedback(models.Model):
    full_name = models.CharField(max_length=225)
    position = models.CharField(max_length=225)
    text = models.TextField()
    star = models.CharField(max_length=5, choices=RATE_CHOICE, null=True, blank=True)


class ConnectWithUs(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
