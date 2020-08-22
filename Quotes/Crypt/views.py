import requests, datetime

from rest_framework import generics, permissions

from .models import CryptQuotes
from .serializers import PriceSerializer


class QuotesList(generics.ListCreateAPIView):
    queryset = CryptQuotes.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (permissions.AllowAny,)
