# Register your models here.
from  apps.crypto.models import CryptoCurrency, LastTrade
from django.contrib import admin


class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ['bot','currency','created_at']
admin.site.register(CryptoCurrency,CryptoCurrencyAdmin)
admin.site.register(LastTrade)
