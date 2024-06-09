from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    registration_date = models.DateField()
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
