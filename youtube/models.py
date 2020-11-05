from django.db import models
from embed_video.fields import EmbedVideoField

class Videos(models.Model):
    name = models.CharField(max_length=200)
    url_id =  models.CharField(max_length=200, blank=True)