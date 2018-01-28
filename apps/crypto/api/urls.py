from rest_framework.routers import DefaultRouter

from apps.crypto.api.views import CryptoCurrencyViewSet, LastTradeViewSet

router = DefaultRouter()

router.register('crypto-currencies', CryptoCurrencyViewSet)
router.register('last-trades',LastTradeViewSet)

urlpatterns = router.urls
