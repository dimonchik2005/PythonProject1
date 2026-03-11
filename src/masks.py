def get_mask_card_number(card_number: str) -> str:
    digits = "".join(ch for ch in card_number if ch.isdigit())
    if len(digits) != 16:
        raise ValueError("Card number must contain 16 digits")

    first6 = digits[:6]
    last4 = digits[-4:]
    return f"{first6[:4]} {first6[4:6]}** **** {last4}"


def get_mask_account(account_number: str) -> str:
    digits = "".join(ch for ch in account_number if ch.isdigit())
    if len(digits) < 4:
        raise ValueError("Account number must contain at least 4 digits")

    return f"**{digits[-4:]}"
