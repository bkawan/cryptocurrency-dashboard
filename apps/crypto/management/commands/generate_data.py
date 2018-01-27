import datetime
import random

from django.core.management import BaseCommand

from apps.crypto.models import CryptoCurrency, LastTrade


class Command(BaseCommand):
    def handle(self, *args, **options):
        bots = ['BOT1', 'BOT2', 'BOT3']
        currencies = ['XRP', 'BTC', 'LTC']
        _last_date = datetime.datetime.now() + datetime.timedelta(days=1)
        CryptoCurrency.objects.all().delete()
        LastTrade.objects.all().delete()
        for i in range(400):
            created_at = _last_date - datetime.timedelta(hours=1)
            for bot in bots:
                for currency in currencies:
                    CryptoCurrency.objects.create(
                        created_at=created_at,
                        bot=bot,
                        currency=currency,
                        profit=random.uniform(0, 100),
                        balance=random.uniform(0, 10000)

                    )
            _last_date = created_at

        _last_date = datetime.datetime.now() + datetime.timedelta(hours=1)
        for i in range(20):
            created_at = _last_date - datetime.timedelta(days=1)
            LastTrade.objects.create(
                info=random.choice(['sell', 'buy']),
                quantity=random.randint(1, 3),
                value="{}{}".format(random.choice(["$", "£", "€"]), random.randint(1, 1000)),
                date=_last_date,
                volume="{}{}".format(random.choice(["$", "£", "€"]), random.randint(1, 1000))

            )
            _last_date = created_at

        print('Created Successfully')
