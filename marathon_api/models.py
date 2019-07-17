from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Photo(models.Model):
    urlOriginal = models.CharField(max_length=1000)
    urlCompressed = models.CharField(max_length=1000)
    watermark = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photographer=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.id, self.urlOriginal, self.watermark, self.event)
