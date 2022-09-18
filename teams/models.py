from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    city = models.CharField(max_length=32, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=32, default='generic-team')

    def __str__(self):
        return self.name