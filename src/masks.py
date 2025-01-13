def get_mask_card_number(card_number: int) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: XXXX XX** **** XXXX"""
    card_number_string = str(card_number)
    return f"{card_number_string[:4]} {card_number_string[4:6]}** **** {card_number_string[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: **XXXX"""
    account_number_string = str(account_number)
    return f"**{account_number_string[-4:]}"
