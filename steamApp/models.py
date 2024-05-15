import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class SteamUser(models.Model):
    steamID = models.IntegerField(primary_key=True)
    realName = models.CharField(max_length=1000)
    personaName = models.CharField(max_length=1000)
    country = models.CharField(max_length=20)
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE)

    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
    products = models.ManyToManyField('Product', blank=True)

    def __str__(self):
        return self.personaName


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appId = models.IntegerField(null=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    free = models.BooleanField()
    recommendations = models.IntegerField(null=True)
    releaseDate = models.DateField()
    categories = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    languages = models.CharField(max_length=300)
    owners = models.IntegerField(null=True)
    description = models.TextField()
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + str(self.releaseDate)




class Developer(models.Model):
    name = models.CharField(max_length=200)
    developedProducts = models.IntegerField(null=True)
    products = models.ManyToManyField('Product', blank=True)
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    publishedProducts = models.IntegerField(null=True)
    products = models.ManyToManyField('Product', blank=True)
    creatorUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
