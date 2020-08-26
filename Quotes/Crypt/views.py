import requests

from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CryptQuotes


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptQuotes
        fields = ('price', 'time')


class QuotesList(generics.ListCreateAPIView):
    queryset = CryptQuotes.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (permissions.AllowAny,)


class QuotesNow(APIView):
    def get(self, request):
        url_param = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        params = {'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd', "id": 1}
        response = requests.get(url_param, params).json()
        return Response(response)
