from django.db import models


# Create your models here.

class User(models.Model):
    steamID = models.IntegerField(primary_key=True)
    realName = models.CharField(max_length=1000)
    personaName = models.CharField(max_length=1000)
    profileUrl = models.URLField()
    countryCode = models.CharField(max_length=10)
    timeCreated = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField('self', symmetrical=True, null=True, blank=True)
    products = models.ManyToManyField('Product', symmetrical=True, null=True, blank=True)


class Product(models.Model):
    appId = models.IntegerField(primary_key=True)
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
    users = models.ManyToManyField('User', symmetrical=True, blank=True, null=True)
    description = models.TextField()
