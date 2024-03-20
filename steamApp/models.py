from django.db import models


# Create your models here.

class User(models.Model):
    steamID = models.IntegerField(primary_key=True)
    realName = models.CharField(max_length=1000)
    personaName = models.CharField(max_length=1000)
    profileUrl = models.URLField()
    countryCode = models.CharField(max_length=10)
    timeCreated = models.DateTimeField(auto_now_add=True)
    friends = models.ManyToManyField('self', symmetrical=True, related_name='friends')
    