import datetime
import random

from django.core.management import BaseCommand

from apps.crypto.models import CryptoCurrency


class Command(BaseCommand):
    def handle(self, *args, **options):
        bots = ['BOT1', 'BOT2', 'BOT3']
        currencies = ['XRP', 'BTC', 'LTC']
        _last_date = datetime.datetime.now()
        CryptoCurrency.objects.all().delete()
        for bot in bots:
            for currency in currencies:
                for i in range(400):
                    created_at = _last_date - datetime.timedelta(days=1)
                    CryptoCurrency.objects.create(
                        created_at=created_at,
                        bot=bot,
                        currency=currency,
                        profit=random.uniform(0, 100),
                        balance=random.uniform(0, 10000)

                    )

        print('Created Successfully')
