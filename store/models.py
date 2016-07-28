from django.db import models


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


# class Cart(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # total_price = models.DecimalField(max_digits=8, decimal_places=2)
    # weight = models.DecimalField(max_digits=8, decimal_places=2)
    # quantity = models.IntegerField()
    # products = models.ManyToManyField(Product)

