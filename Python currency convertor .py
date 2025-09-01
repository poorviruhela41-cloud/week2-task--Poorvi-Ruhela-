#-*- coding: utf-8-*-
import requests

class CurrencyConverter:
    def __init__(self, base_currency="USD"):
        self.base_currency = base_currency
        self.rates = self.get_rates()

    def get_rates(self):
        url = f"https://open.er-api.com/v6/latest/{self.base_currency}"
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            return data["rates"]
        else:
            raise Exception("Error fetching exchange rates")

    def convert(self, amount, target_currency):
        if target_currency in self.rates:
            converted_amount = amount * self.rates[target_currency]
            return converted_amount
        else:
            raise ValueError("Invalid currency code!")

def main():
    print(" Currency Converter (using ExchangeRate API)")
    base = input("Enter base currency (e.g., USD, INR, EUR): ").upper()
    converter = CurrencyConverter(base)

    amount = float(input(f"Enter amount in {base}: "))
    target = input("Enter target currency: ").upper()

    try:
        result = converter.convert(amount, target)
        print(f"{amount} {base} = {result:.2f} {target}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()