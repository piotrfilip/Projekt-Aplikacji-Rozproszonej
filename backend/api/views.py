import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class CurrencyRatesView(APIView):
    def get(self, request, *args, **kwargs):
        response = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
        data = response.json()
        return Response(data)
