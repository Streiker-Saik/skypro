from typing import Dict, Iterator, List, Union


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """Функция получает список словарей транзакций и наименование валюты,
    возвращает итератор транзакций отфильтрованный по наименованию валюты"""
    return filter(
        lambda code_currency: code_currency.get("operationAmount", 0).get("currency", 0).get("code", 0) == currency,
        transactions,
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", 0)


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Union[List[str], TypeError, ValueError]:
    """Функция принимает целое число начало диапазона и конца,
    выдает список номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Неуказанный диапазон от 1 до 9999999999999999(16 цифр)"""

    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Введено не числовое значение")

    if start < 1 or stop > 9999999999999999:
        raise ValueError("Введены числа не в диапазоне с 1 до 9999999999999999(16 цифр)")

    numbers = []

    for number in range(start, stop + 1):
        format_number = str("{:16d}".format(number)).replace(" ", "0")
        card_number_string = f"{format_number[:4]} {format_number[4:8]} {format_number[8:12]} {format_number[12:]}"
        numbers.append(card_number_string)

    return numbers
