from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class DSProject(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    objects = models.Manager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
