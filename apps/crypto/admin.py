# Register your models here.
from  apps.crypto.models import CryptoCurrency, LastTrade
from django.contrib import admin

admin.site.register(CryptoCurrency)
admin.site.register(LastTrade)
