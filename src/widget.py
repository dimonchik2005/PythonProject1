from src.masks import get_mask_account, get_mask_card_number


# обрабатывает информацию как о картах, так и о счетах
def mask_account_card(data: str) -> str:
    parts = data.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if name.lower() == "счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


# ринимает на вход строку с датой в формате  "2024-03-11T02:26:18.671407"
# и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
def get_date(date_string: str) -> str:
    date_part = date_string[:10]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
