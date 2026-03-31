import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "data, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
    ],
)
def test_mask_account_card_for_cards(data: str, expected: str) -> None:
    assert mask_account_card(data) == expected


def test_mask_account_card_for_account() -> None:
    assert mask_account_card("Счет 12345678") == "Счет **5678"


def test_mask_account_card_empty_string() -> None:
    with pytest.raises(IndexError):
        mask_account_card("")


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-01", "01.12.2023"),
    ],
)
def test_get_date_valid(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


def test_get_date_invalid_format() -> None:
    with pytest.raises(ValueError):
        get_date("invalid-date")
