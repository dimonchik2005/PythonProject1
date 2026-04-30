from unittest.mock import Mock, patch

from src.external_api import convert_transaction_amount_to_rub


def test_convert_transaction_amount_rub() -> None:
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"},
        }
    }

    assert convert_transaction_amount_to_rub(transaction) == 100.50


@patch("src.external_api.requests.get")
def test_convert_transaction_amount_usd(mock_get: Mock) -> None:
    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"},
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {"result": 9000.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    assert convert_transaction_amount_to_rub(transaction) == 9000.0


@patch("src.external_api.requests.get")
def test_convert_transaction_amount_eur(mock_get: Mock) -> None:
    transaction = {
        "operationAmount": {
            "amount": "50",
            "currency": {"code": "EUR"},
        }
    }

    mock_response = Mock()
    mock_response.json.return_value = {"result": 5000.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    assert convert_transaction_amount_to_rub(transaction) == 5000.0
