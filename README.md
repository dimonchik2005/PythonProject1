# Банковский виджет

## Описание проекта
Проект реализует обработку банковских операций:
- маскировка номеров карт и счетов;
- форматирование дат;
- фильтрация операций по статусу;
- сортировка операций по дате.

## Структура проекта
- `src/masks.py` — маскировка карты и счета
- `src/widget.py` — обработка строк с картами/счетами и датами
- `src/processing.py` — фильтрация и сортировка операций
- `tests/` — тесты

## Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/dimonchik2005/PythonProject1.git
```

## Тестирование

Для запуска тестов выполните команду:

```bash
poetry run pytest
```
## Модуль decorators

Модуль `decorators` содержит декоратор `log`, который логирует результат выполнения функции.

Если передан параметр `filename`, лог записывается в файл.  
Если `filename` не передан, лог выводится в консоль.

Пример:

```python
from src.decorators import log


@log(filename="mylog.txt")
def add(x: int, y: int) -> int:
    return x + y


add(1, 2)
```
Результат при успешном выполнении:
```bash
add ok
```
Результат при ошибке:
```
add error: ZeroDivisionError. Inputs: (1, 0), {}
```
## Чтение CSV- и Excel-файлов

Добавлен модуль `file_readers`, который позволяет считывать финансовые операции из CSV- и Excel-файлов.

### CSV

```python
from src.file_readers import read_transactions_from_csv

transactions = read_transactions_from_csv("data/transactions.csv")
```