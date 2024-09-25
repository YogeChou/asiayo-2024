class CurrencyService:
    def __init__(self):
        self.rate = {
            "TWD": 1,
            "USD": 31
        }

    def get_rate(self, currency):
        if currency not in self.rate:
            raise ValueError("Currency format is wrong")
        return self.rate[currency]
