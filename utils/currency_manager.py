from environs import Env
import requests
import logging


# environment variables load
utils_env_var = Env()
utils_env_var.read_env("environs/.env.utils")


# logging init
logger = logging.getLogger(__name__)


# Manager based on free api : https://openexchangerates.org/
class CurrencyExchangeManager:
    """ Manager class to perform currency exchange calculating operations. """

    BASE_API_ENDPOINT = "https://openexchangerates.org/api/"
    APP_ID = utils_env_var("CURRENCY_MANAGER_API_TOKEN")

    @classmethod
    def get_last_exchange_rates(cls, base: str = "USD", currency_to_exchange: str | None = None) -> dict:
        """ Returns latest exchange rates between base currency and currency to exchange. 
        If currency_to_exchange is not provided returns all currencies exchange raters for base currency.
        By default, base currency is 'USD'."""
        logger.debug(f"Method 'get_last_exchange_rates' requested with parameters: {base:} and {currency_to_exchange:}")

        response = requests.get(cls.BASE_API_ENDPOINT + f"latest.json", params={"app_id": cls.APP_ID, "base": base})
        # retrieving latest currencies' latest exchange rates
        currency_latest_exchange_rates = response.json().get("rates")
        if currency_to_exchange is None:
            return currency_latest_exchange_rates
        # retrieving currency exchange rate for the currency specified (if so)
        else:
            return {
                "currency_to_exchange": currency_to_exchange,
                "rate": currency_latest_exchange_rates.get(currency_to_exchange.upper())
            }

    @classmethod
    def currency_converter(cls, value: int, exchange_to: str, base: str = "USD") -> int:
        """ Converts two currencies.
         Where 'base' value is a value converted from and 'exchange_to' is a result currency."""
        logger.debug(f"Method 'currency_converter' requested with parameters: {value:}, {exchange_to}, {base:}")
        # retrieving latest currencies' exchange rates
        exchange_rate = cls.get_last_exchange_rates(base=base, currency_to_exchange=exchange_to).get("rate")
        # converting 'base' currency's value to 'exchange_to' currency's value:
        converted_value = float(value) * exchange_rate
        return converted_value
