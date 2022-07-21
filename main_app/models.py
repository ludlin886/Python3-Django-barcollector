from django.db import models
from django.urls import reverse

class Bar(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bar_id': self.id})