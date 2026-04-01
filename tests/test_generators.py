import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "currency, expected_len",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),
    ],
)
def test_filter_by_currency(
    transactions_for_generators: list[dict],
    currency: str,
    expected_len: int,
) -> None:
    result = list(filter_by_currency(transactions_for_generators, currency))
    assert len(result) == expected_len


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions_for_generators: list[dict]) -> None:
    result = list(transaction_descriptions(transactions_for_generators))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            9,
            10,
            [
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_single() -> None:
    assert list(card_number_generator(1, 1)) == ["0000 0000 0000 0001"]
