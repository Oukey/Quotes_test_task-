import requests, datetime

from rest_framework import generics, permissions, serializers

from .models import CryptQuotes


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptQuotes
        fields = ('price', 'time')


class QuotesList(generics.ListCreateAPIView):
    queryset = CryptQuotes.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (permissions.AllowAny,)
