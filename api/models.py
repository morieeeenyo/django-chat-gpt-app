from django.db import models


# Create your models here.
class Threads(models.Model):
    title = models.CharField(max_length=256)


class Messages(models.Model):
    text = models.TimeField(null=False)
    thread = models.ForeignKey(Threads, on_delete=models.CASCADE)
