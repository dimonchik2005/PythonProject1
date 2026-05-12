import json
import logging
from pathlib import Path
from typing import Any

LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

utils_file_handler = logging.FileHandler(
    LOGS_DIR / "utils.log",
    mode="w",
    encoding="utf-8",
)
utils_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)

if not utils_logger.handlers:
    utils_logger.addHandler(utils_file_handler)


def read_json_file(file_path: str) -> list[dict[str, Any]]:
    """Возвращает список транзакций из JSON-файла."""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        utils_logger.error("Файл не найден: %s", file_path)
        return []
    except json.JSONDecodeError:
        utils_logger.error("Некорректный JSON-file: %s", file_path)
        return []

    if not isinstance(data, list):
        utils_logger.error("JSON данный не являются списком: %s", file_path)
        return []

    utils_logger.info("JSON-file успешно прочитан: %s", file_path)
    return data
