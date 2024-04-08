from django.contrib import admin
from .models import SteamUser, Product, Developer, Publisher

# Register your models here.
admin.site.register(SteamUser)
admin.site.register(Product)
admin.site.register(Developer)
admin.site.register(Publisher)