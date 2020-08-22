from Quotes.Quotes.celery import app
from .models import CryptQuotes
import requests


def price():
    url_param = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
               "Accept": "application/json"}
    params = {"id": 1}
    response = requests.get(url_param, params, headers).json()
    return {'price': response['data']['1']['quote']['USD']['price']}


@app.task
def get_price():
    data = price()
    CryptQuotes.objects.create(price=data['price'])
