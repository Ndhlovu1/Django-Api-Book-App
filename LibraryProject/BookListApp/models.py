from django.db import models


# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]


