import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurrencyConventore:
    @staticmethod
    def convert(qoute: str, base: str, amount: str):
        if qoute == base:
            raise ConvertionException('Нельзя перевести валюту в саму себя! ')

        try:
            qoute_ticker = keys[qoute]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {qoute}!')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base