from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    date_part = date_string[:10]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"