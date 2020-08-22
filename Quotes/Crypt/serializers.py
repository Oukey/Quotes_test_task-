from rest_framework import serializers
from .models import CryptQuotes


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptQuotes
        fields = ('price', 'time')
