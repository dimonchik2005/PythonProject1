import json
from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_success() -> None:
    test_data = [{"id": 1, "amount": "100"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        assert read_json_file("test.json") == test_data


def test_read_json_file_not_found() -> None:
    assert read_json_file("missing.json") == []


def test_read_json_file_empty() -> None:
    with patch("builtins.open", mock_open(read_data="")):
        assert read_json_file("empty.json") == []


def test_read_json_file_not_list() -> None:
    with patch("builtins.open", mock_open(read_data='{"id": 1}')):
        assert read_json_file("not_list.json") == []
