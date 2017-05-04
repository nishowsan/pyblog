from django.db import models


class Blog(models.Model):
    header = models.CharField(max_length=600)
    body = models.CharField(max_length=1000000)
    picture = models.FileField()

    def __str__(self):
        return self.header
