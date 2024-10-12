from django.db import models

class ProductSales(models.Model):
    product = models.CharField(max_length=100)
    sales = models.PositiveIntegerField()
    region = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.product} - {self.sales} - {self.region}"
