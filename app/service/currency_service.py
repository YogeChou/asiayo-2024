from abc import ABC, abstractmethod


class Currency(ABC):

    @abstractmethod
    def get_conversion_rate(self, to_currency: str) -> float:
        """取得當前貨幣與其他貨幣的轉換匯率"""
        pass


class USD(Currency):
    def get_conversion_rate(self, to_currency: str) -> float:
        rates = {
            "TWD": 31.0,
            "EUR": 0.85,
            "JPY": 110.0
        }
        return rates.get(to_currency, 1)


class TWD(Currency):
    def get_conversion_rate(self, to_currency: str) -> float:
        rates = {
            "USD": 0.032,
            "EUR": 0.027,
            "JPY": 3.5
        }
        return rates.get(to_currency, 1)


class CurrencyConverter:
    def __init__(self, base_currency: Currency):
        self.base_currency = base_currency

    def convert(self, amount: float, to_currency: str) -> float:
        rate = self.base_currency.get_conversion_rate(to_currency)
        return amount * rate


class CurrencyFactory:
    @staticmethod
    def get_currency(currency_code: str) -> Currency:
        currency_map = {
            "USD": USD(),
            "TWD": TWD(),
        }
        return currency_map.get(currency_code.upper(), USD())
