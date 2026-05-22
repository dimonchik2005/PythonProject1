from typing import Any

from src.search import process_bank_operations, process_bank_search


def test_process_bank_search_found() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод с карты на карту"},
    ]

    result = process_bank_search(data, "Перевод")

    assert result == [
        {"id": 1, "description": "Перевод организации"},
        {"id": 3, "description": "Перевод с карты на карту"},
    ]


def test_process_bank_search_ignore_case() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
    ]

    result = process_bank_search(data, "перевод")

    assert result == [
        {"id": 1, "description": "Перевод организации"},
    ]


def test_process_bank_search_not_found() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
    ]

    assert process_bank_search(data, "Оплата") == []


def test_process_bank_search_empty_list() -> None:
    assert process_bank_search([], "Перевод") == []


def test_process_bank_search_without_description() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1},
        {"id": 2, "description": "Перевод организации"},
    ]

    result = process_bank_search(data, "Перевод")

    assert result == [
        {"id": 2, "description": "Перевод организации"},
    ]


def test_process_bank_operations() -> None:
    data: list[dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод организации"},
        {"id": 4, "description": "Перевод с карты на карту"},
    ]

    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
        "Перевод со счета на счет",
    ]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
        "Перевод со счета на счет": 0,
    }


def test_process_bank_operations_empty_list() -> None:
    categories = ["Перевод организации", "Открытие вклада"]

    assert process_bank_operations([], categories) == {
        "Перевод организации": 0,
        "Открытие вклада": 0,
    }
