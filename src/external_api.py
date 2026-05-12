import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_transaction_amount_to_rub(transaction: dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"

    response = requests.get(
        url,
        headers={"apikey": api_key},
        params={"from": currency_code, "to": "RUB", "amount": amount},
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()
    return float(data["result"])
