from django.db import models
from django.contrib.auth.models import User


class AbstractAddress(models.Model):
    address1 = models.CharField(blank=True, max_length=255)
    address2 = models.CharField(blank=True, max_length=255)
    city = models.CharField(blank=True, max_length=255)
    state = models.CharField(null=True, blank=True, max_length=255)
    zip_code = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        abstract = True

# auth.models.User has: 1) username 2) password 3) email 4) first_name 5) surname
class UserProfile(AbstractAddress, models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Pet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    pet_type = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    sex = models.CharField(blank=True, max_length=10)
    age = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


