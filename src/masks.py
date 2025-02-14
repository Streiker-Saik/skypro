from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: XXXX XX** **** XXXX"""

    if card_number is None:
        raise TypeError("Вводные дынные отсутствуют")

    if not isinstance(card_number, (int, str)):
        raise TypeError("Введен не корректный тип данных")

    card_number_string = str(card_number)

    if len(card_number_string) != 16 or not card_number_string.isdigit():
        raise ValueError("В номере карты должно быть 16 цифр")

    return f"{card_number_string[-16:-12]} {card_number_string[-12:-10]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: **XXXX"""

    if account_number is None:
        raise TypeError("Вводные дынные отсутствуют")

    if not isinstance(account_number, (int, str)):
        raise TypeError("Введен не корректный тип данных")

    account_number_string = str(account_number)

    if len(account_number_string) != 20 or not account_number_string.isdigit():
        raise ValueError("В номере счета должно быть 20 цифр")

    return f"**{account_number_string[-4:]}"
