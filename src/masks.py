from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: XXXX XX** **** XXXX"""
    card_number_string = str(card_number)
    return f"{card_number_string[-16:-12]} {card_number_string[-12:-10]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: **XXXX"""
    account_number_string = str(account_number)
    return f"**{account_number_string[-4:]}"
