from django.urls import path
from .views import CurrencyRatesView

urlpatterns = [
    path('currencies/', CurrencyRatesView.as_view(), name='currency-rates'),
]
