from django.db import models


class Player(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    registration_date = models.DateField()
    level = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)


class Group(models.Model):
    name = models.CharField(max_length=31)
    slogan = models.CharField(max_length=127)
    description = models.CharField(max_length=2047)
    members_count = models.IntegerField(default=1)
    lieder = models.OneToOneField('Player', on_delete=models.PROTECT, related_name='lieder_group')
