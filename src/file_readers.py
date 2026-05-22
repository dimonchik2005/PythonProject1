from typing import Any, cast

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict[str, Any]]:
    """Возвращает список транзакций из CSV-файла."""
    try:
        dataframe = pd.read_csv(file_path, sep=";")
    except FileNotFoundError:
        return []

    return cast(list[dict[str, Any]], dataframe.to_dict(orient="records"))


def read_transactions_from_excel(file_path: str) -> list[dict[str, Any]]:
    """Возвращает список транзакций из Excel-файла."""
    try:
        dataframe = pd.read_excel(file_path)
    except FileNotFoundError:
        return []

    return cast(list[dict[str, Any]], dataframe.to_dict(orient="records"))
