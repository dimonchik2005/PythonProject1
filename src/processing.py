from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """Возвращает список операций, отфильтрованный по значению ключа state."""
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]],
    reverse: bool = True,
) -> list[dict[str, Any]]:
    """Возвращает новый список операций, отсортированный по дате."""
    return sorted(operations, key=lambda operation: operation["date"], reverse=reverse)
