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
    def get_last_exchange_rates(cls, currency_to_exchange: str, base: str = "USD") -> dict:
        """ Returns latest exchange rates between 'base' currency and 'currency_to_exchange'."""
        logger.debug(f"Method 'get_last_exchange_rates' requested with parameters: {base:}, {currency_to_exchange:}")

        response = requests.get(cls.BASE_API_ENDPOINT + f"latest.json", params={"app_id": cls.APP_ID})
        # retrieving latest currencies' exchange rates for USD
        currency_latest_exchange_rates = response.json().get("rates")
        match base:
            case "USD":
                # returns exchange rate of 'currency_to_exchange' relative to USD
                exchange_rate = currency_latest_exchange_rates.get(currency_to_exchange.upper())
            case _:
                # performing conversion between 'base' and 'currency_to_exchange' through USD as intermediate currency
                base_currency_to_usd_rate = currency_latest_exchange_rates.get(base)
                income_currency_to_usd_rate = currency_latest_exchange_rates.get(currency_to_exchange)
                exchange_rate = income_currency_to_usd_rate / base_currency_to_usd_rate

        # retrieving currency exchange rate for the currency specified
        return {
            "base": base,
            "currency_to_exchange": currency_to_exchange,
            "rate": exchange_rate
        }

    @classmethod
    def currency_converter(cls, value: int, exchange_to: str, base: str = "USD") -> int:
        """ Converts two currencies.
         Where 'value' parameter is an amount to be converted from 'base' currency to 'exchange_to' currency."""
        logger.debug(f"Method 'currency_converter' requested with parameters: {value:}, {exchange_to}, {base:}")

        # retrieving latest currencies' exchange rates
        exchange_rate = cls.get_last_exchange_rates(currency_to_exchange=exchange_to, base=base).get("rate")
        # converting 'base' currency's value to 'exchange_to' currency's value:
        converted_value = float(value) * exchange_rate
        return converted_value
