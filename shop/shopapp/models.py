from django.db import models

# Create your models here.
class Item(models.Model):
    url = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    user = models.CharField(max_length=1000)

    def __str__(self):
            return self.image