from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Job(models.Model):
    title   = models.CharField(max_length=256)
    url     = models.URLField(max_length=512)
    body    = models.TextField()
    status  = models.BooleanField(default=1)

    def __str__(self):
        return self.title
