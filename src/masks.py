import logging
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

masks_file_handler = logging.FileHandler(
    LOGS_DIR / "masks.log",
    mode="w",
    encoding="utf-8",
)
masks_file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)

if not masks_logger.handlers:
    masks_logger.addHandler(masks_file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера банковской карты."""
    digits = "".join(ch for ch in card_number if ch.isdigit())

    if len(digits) != 16:
        masks_logger.error("Некорректная длина номера карты")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    result = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    masks_logger.info("Номер карты успешно замаскирован")
    return result


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета."""
    digits = "".join(ch for ch in account_number if ch.isdigit())

    if len(digits) < 4:
        masks_logger.error("Неверная длина номера счета.")
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    result = f"**{digits[-4:]}"
    masks_logger.info("Номер счета успешно замаскирован")
    return result
