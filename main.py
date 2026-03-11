from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    choice = input("Что замаскировать? (card/account): ").strip().lower()

    if choice == "card":
        number = input("Введите номер карты: ").strip()
        print(get_mask_card_number(number))
    elif choice == "account":
        number = input("Введите номер счета: ").strip()
        print(get_mask_account(number))
    else:
        print("Неверный выбор. Введите card или account.")


if __name__ == "__main__":
    main()
