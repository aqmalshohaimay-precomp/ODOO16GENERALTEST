import requests


class CurrencyExchangeModule:
    def __init__(self):
        self.api_url = "https://api.exchangeratesapi.io/v1/latest?access_key=5fd0f32772d4b3077e0e87c84baa838e&format=1"

    def get_exchange_rates(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            data = response.json()

            # Extracting relevant information
            base_currency = "MYR"
            exchange_date = data["date"]
            exchange_rates = data["rates"]

            return base_currency, exchange_date, exchange_rates
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that may occur during the request
            print(f"Error fetching exchange rates: {e}")
            return None


# Example usage
if __name__ == "__main__":
    currency_module = CurrencyExchangeModule()
    result = currency_module.get_exchange_rates()

    if result:
        base_currency, exchange_date, exchange_rates = result
        print(f"Base Currency: {base_currency}")
        print(f"Exchange Date: {exchange_date}")
        print("Exchange Rates:")
        for currency, rate in exchange_rates.items():
            print(f"{currency}: {rate}")
    else:
        print("Failed to fetch exchange rates.")
