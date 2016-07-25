from django.db import models

# Create your models here.

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

# class User(models.Model):
    # user = models.OneToOneField(User)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # email = models.EmailField()


# class Pet(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # name = models.CharField(max_length=255)
    # pet_type = models.CharField(max_length=255)
    # sex = models.CharField(max_length=10)
    # age = models.IntegerField()
    # weight = models.IntegerField()
    # owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # breed_id = models.ForeignKey(Breed, on_delete=models.CASCADE)

# class Breed(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

# class Cart(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # total_price = models.DecimalField(max_digits=8, decimal_places=2)
    # weight = models.DecimalField(max_digits=8, decimal_places=2)
    # quantity = models.IntegerField()
    # products = models.ManyToManyField(Product)

