from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageUrl = models.URLField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title