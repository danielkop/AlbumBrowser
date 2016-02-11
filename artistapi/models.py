from __future__ import unicode_literals
from django.db import models
from collections import OrderedDict

class Artist(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
		
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    date_released = models.DateTimeField('Date Released')
    image = models.CharField(max_length=256)
    actualArtist = models.CharField(max_length=128)
    def __str__(self):
		return self.name
    def __unicode__(self):
        return self.name
		
    def as_dict(self):
			album_dict = OrderedDict()
			album_dict["name"] = self.name
			album_dict["image"] = self.image
			album_dict["release_date"] = self.date_released
			album_dict["actualArtist"] = self.actualArtist
			return album_dict
