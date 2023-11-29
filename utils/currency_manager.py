from environs import Env
import requests


# environment variables load
utils_env_var = Env()
utils_env_var.read_env("environs/.env.utils")

# Manager based on free api : https://openexchangerates.org/
class CurrencyExchangeManager:
    """ Manager class to perform currency exchange calculating operations. """
    
    BASE_API_ENDPOINT = "https://openexchangerates.org/api/"
    
    def __init__(self, api_token: str = utils_env_var("CURRENCY_MANAGER_API_TOKEN")) -> None:
        self.api_token = api_token
    
    def get_last_exchange_rates(self, base: str = "USD", currency_to_exchange: str | None = None) -> dict:
        """ Returns latest exchange rates between base currency and currency to exchange. 
        If currency_to_exchange is not provided returns all currencies exchange raters for base currency.
        By default base currency is 'USD'."""
        
        response = requests.get(
            self.BASE_API_ENDPOINT + f"latest.json", 
            params={"app_id": self.api_token, "base": base}
            )
        currency_latest_exchange_rates = response.json().get("rates")
        if currency_to_exchange is None:
            return currency_latest_exchange_rates
        else:
            return {
                "currency_to_exchange": currency_to_exchange,
                "rate": currency_latest_exchange_rates.get(currency_to_exchange.upper())
                }
    
    def currency_converter(self, base: str = "USD", convert_to_currency: str | None = None) -> int:
        pass



if __name__ == "__main__":
    exchange_manager = CurrencyExchangeManager()
    print(exchange_manager.get_last_exchange_rates("USD", "UAH"))

