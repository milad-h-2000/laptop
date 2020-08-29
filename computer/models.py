from django.db import models


class Computer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='computer\\images', null=True)
    date = models.DateField()
    price = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
