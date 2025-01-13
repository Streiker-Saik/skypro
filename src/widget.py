from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card_account: str) -> str:
    """Функция принимает "название карты" "номер" или "счет" и выводит через f строку название и маску"""
    if number_card_account.count(" ") == 1:
        index_space = number_card_account.index(" ")
    else:
        index_space = number_card_account.find(" ", number_card_account.find(" ") + 1)
    return (
        f"{number_card_account[:index_space]} {get_mask_account(number_card_account)}"
        if number_card_account[:index_space] == "Счет"
        else f"{number_card_account[:index_space]} {get_mask_card_number(number_card_account)}"
    )


def get_date(data: str) -> str:
    """Функция принимает дату и время в формате ГГГГ-ММ-ДД... и выводит дату в формате ДД.ММ.ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
