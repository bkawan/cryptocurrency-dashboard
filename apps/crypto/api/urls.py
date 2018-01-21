from rest_framework.routers import DefaultRouter

from apps.crypto.api.views import CryptoCurrencyViewSet

router = DefaultRouter()

router.register('crypto-currencies', CryptoCurrencyViewSet)

urlpatterns = router.urls
