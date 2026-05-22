from typing import Any

from src.file_readers import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def load_transactions(user_choice: str) -> list[dict[str, Any]]:
    """Загружает транзакции из выбранного пользователем источника."""
    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        return read_json_file("data/operations.json")

    if user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        return read_transactions_from_csv("data/transactions.csv")

    if user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return read_transactions_from_excel("data/transactions_excel.xlsx")

    print("Неверный пункт меню.")
    return []


def get_valid_status() -> str:
    """Запрашивает у пользователя корректный статус операции."""
    available_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()

        if status in available_statuses:
            print(f'Операции отфильтрованы по статусу "{status}"')
            return status

        print(f'Статус операции "{status}" недоступен.')


def filter_rub_transactions(
    transactions: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Возвращает только рублевые транзакции."""
    return [
        transaction
        for transaction in transactions
        if transaction.get("currency_code") == "RUB"
        or transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
    ]


def get_transaction_amount(transaction: dict[str, Any]) -> str:
    """Возвращает сумму и валюту транзакции."""
    if "operationAmount" in transaction:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]
    else:
        amount = transaction.get("amount")
        currency = transaction.get("currency_code")

    return f"{amount} {currency}"


def print_transactions(transactions: list[dict[str, Any]]) -> None:
    """Выводит список транзакций в консоль."""
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        date = get_date(transaction["date"])
        description = transaction["description"]
        amount = get_transaction_amount(transaction)

        print()
        print(f"{date} {description}")

        from_account = transaction.get("from")
        to_account = transaction.get("to")

        if isinstance(from_account, str) and isinstance(to_account, str):
            print(f"{mask_account_card(from_account)} -> {mask_account_card(to_account)}")
        elif isinstance(to_account, str):
            print(mask_account_card(to_account))

        print(f"Сумма: {amount}")


def main() -> None:
    """Запускает пользовательский сценарий работы с транзакциями."""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    user_choice = input()
    transactions = load_transactions(user_choice)

    status = get_valid_status()
    transactions = filter_by_state(transactions, status)

    sort_answer = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_answer == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        reverse = sort_order != "по возрастанию"
        transactions = sort_by_date(transactions, reverse=reverse)

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()

    if rub_answer == "да":
        transactions = filter_rub_transactions(transactions)

    search_answer = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    )

    if search_answer == "да":
        search_word = input("Введите слово для поиска в описании:\n")
        transactions = process_bank_search(transactions, search_word)

    print_transactions(transactions)


if __name__ == "__main__":
    main()
