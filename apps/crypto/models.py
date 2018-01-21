from django.db import models

# Create your models here.
CURRENCY_CHOICES = (
    ('XRP', 'XRP'),
    ('BTC', 'BTC'),
    ('LTC', 'LTC'),
)
BOT_CHOICES = (
    ('BOT1', 'BOT1'),
    ('BOT2', 'BOT2'),
    ('BOT3', 'BOT3'),
)


class CryptoCurrency(models.Model):
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10)
    bot = models.CharField(choices=BOT_CHOICES, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    profit = models.FloatField()
    balance = models.FloatField()

    def __str__(self):
        return "{}-{}-{}".format(self.bot, self.currency, self.created_at)


class LastTrade(models.Model):
    info = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return "{}-{}-{}".format(self.info, self.quantity, self.value)
