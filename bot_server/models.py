from django.db import models


class Data(models.Model):
    FAT_COUNT       = models.IntegerField()
    STUPID_COUNT    = models.IntegerField()
    DUMB_COUNT      = models.IntegerField()

