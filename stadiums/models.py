from django.db import models

# Create your models here.
class Stadium(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    address = models.CharField(max_length=64, null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False)
    location = models.CharField(max_length=32, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=32, default='generic-stadium')

    def __str__(self):
        return self.name