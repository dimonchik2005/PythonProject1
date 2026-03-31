import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234-5678-9012-3456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234")


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678", "**5678"),
        ("00001234", "**1234"),
        ("12 34 56 78", "**5678"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_account("123")





