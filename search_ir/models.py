from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    name = models.TextField()
    text = models.TextField()

    def __unicode__(self):
        return self.name