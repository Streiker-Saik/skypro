from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account: Union[str, int, None]) -> Union[str, TypeError]:
    """Функция принимает "название карты" "номер" или "счет" и выводит через f строку название и маску"""

    result = ""

    if card_account is None:
        raise TypeError("Вводные дынные отсутствуют")

    if not isinstance(card_account, str):
        raise TypeError("Введено не строковое значение")

    words = card_account.split()

    for word in words:

        if word.isalpha():
            result += word + " "

        elif word.isdigit():
            if result == "Счет ":
                number = int(word)
                number_mask = get_mask_account(number)
                # result += get_mask_account(number)
            else:
                number = int(word)
                number_mask = get_mask_card_number(number)
                # result += get_mask_card_number(number)

    return f"{result}{number_mask}"


def get_date(data: Union[str, int, None]) -> Union[str, TypeError, ValueError]:
    """Функция принимает дату и время в формате ГГГГ-ММ-ДД... и выводит дату в формате ДД.ММ.ГГГГ"""

    if data is None:
        raise TypeError("Вводные дынные отсутствуют")

    if not isinstance(data, str):
        raise TypeError("Введено не строковое значение")

    day = data[8:10]
    month = data[5:7]
    year = data[:4]

    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        raise ValueError("Вводные дынные некорректны")
    elif not len(day) == 2 or not len(month) == 2 or not len(year) == 4:
        raise ValueError("Вводные дынные некорректны")
    elif not 1 <= int(day) <= 31 or not 1 <= int(month) <= 12 or not 1990 <= int(year) <= 2030:
        raise ValueError("Вводные дынные некорректны")

    return f"{day}.{month}.{year}"
