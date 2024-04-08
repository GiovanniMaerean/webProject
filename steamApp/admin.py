from django.contrib import admin
from .models import SteamUser, Product

# Register your models here.
admin.site.register(SteamUser)
admin.site.register(Product)