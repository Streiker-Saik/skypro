from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Функция получает список словарей транзакций и наименование валюты,
    возвращает итератор транзакций отфильтрованный по наименованию валюты
    """
    return filter(
        lambda code_currency: code_currency.get("operationAmount", 0).get("currency", 0).get("code", 0) == currency,
        transactions,
    )


# Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
def transaction_descriptions():
    pass


# Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
# Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
def card_number_generator():
    pass
