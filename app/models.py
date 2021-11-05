from django.db import models


# Create your models here.
class Pong(models.Model):
    name = models.CharField('name', max_length=150, blank=True)
