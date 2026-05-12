from unittest.mock import Mock, patch

from src.file_readers import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)


@patch("src.file_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv: Mock) -> None:
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    mock_read_csv.return_value = mock_dataframe

    result = read_transactions_from_csv("data/transactions.csv")

    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    mock_read_csv.assert_called_once_with("data/transactions.csv", sep=";")


@patch("src.file_readers.pd.read_csv")
def test_read_transactions_from_csv_file_not_found(mock_read_csv: Mock) -> None:
    mock_read_csv.side_effect = FileNotFoundError

    result = read_transactions_from_csv("missing.csv")

    assert result == []


@patch("src.file_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel: Mock) -> None:
    mock_dataframe = Mock()
    mock_dataframe.to_dict.return_value = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    mock_read_excel.return_value = mock_dataframe

    result = read_transactions_from_excel("data/transactions_excel.xlsx")

    assert result == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
    ]
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")


@patch("src.file_readers.pd.read_excel")
def test_read_transactions_from_excel_file_not_found(mock_read_excel: Mock) -> None:
    mock_read_excel.side_effect = FileNotFoundError

    result = read_transactions_from_excel("missing.xlsx")

    assert result == []
