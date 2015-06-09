import re
from django.db import models
from django.contrib.auth.models import User

class DiaryItem(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64, blank=True)
    link = models.URLField(blank=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField(blank=True)
    end_time = models.TimeField(blank=True)
    author = models.ForeignKey(User)
    location = models.ForeignKey('EventLocation')
    content = models.TextField()
    def __unicode__(self):
        return (self.title)
    def shortened_link(self):
        if self.link:
            return re.sub(r"https?://", '', self.link, flags=re.IGNORECASE)

class EventLocation(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    def __unicode__(self):
        return self.name

class ImageItem(models.Model):
    data = models.ImageField(upload_to="images")
    diary_item = models.ForeignKey(DiaryItem)
