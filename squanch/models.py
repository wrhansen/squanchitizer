from django.db import models

# Create your models here.
class Squanch(models.Model):
    text = models.TextField()
    user = models.CharField(max_length=64)
    squanch_count = models.IntegerField()
