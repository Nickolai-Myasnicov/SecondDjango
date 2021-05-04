from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    cost = models.FloatField(default=0.0)