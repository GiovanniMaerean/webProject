from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SteamUser)
admin.site.register(Product)
admin.site.register(Developer)
admin.site.register(Publisher)
