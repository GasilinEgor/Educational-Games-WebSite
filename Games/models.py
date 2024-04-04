from django.db import models


class SpeedScoreRecords(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()
    date = models.DateField()
