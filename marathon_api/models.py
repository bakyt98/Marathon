from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Photo(models.Model):
    original = models.ImageField(upload_to='images/')
    # urlOriginal = models.CharField(max_length=1000, blank=True, null=True)
    urlCompressed = models.CharField(max_length=1000, blank=True, null=True)
    watermark = models.CharField(max_length=100, blank=True, default='')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tags = models.ManyToManyField("self")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.id, self.watermark, self.event, self.created_by)

    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
        filePath = self.original.url

    @property
    def taglist(self):
        return list(self.tags.all())
