from collections.abc import Generator
from typing import Any


def filter_by_currency(
    transactions: list[dict[str, Any]], currency_code: str
) -> Generator[dict[str, Any], None, None]:
    """Возвращает транзакции с указанным кодом валюты."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Generator[str, None, None]:
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
