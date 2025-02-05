import pytest

from typing import List, Dict, Tuple, Callable

from src.generators import filter_by_currency


def test_filter_by_currency(transactions: List[Dict], input_by_currency: Tuple[str, List[Dict]]) -> None:
    """Тестирование, что функция корректно фильтрует транзакции по заданной валюте"""
    currency, expected = input_by_currency
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_filter_by_currency_not_currency(transactions: List[Dict]) -> None:
    """Тестирование, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют"""
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_not_transactions() -> None:
    """Генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций"""
    result = list(filter_by_currency([], "EUR"))
    assert result == []


# Проверьте, что функция возвращает корректные описания для каждой транзакции.
# Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
def test_transaction_descriptions():
    pass


# Напишите тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
# Проверьте корректность форматирования номеров карт.
# Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.
def test_card_number_generator():
    pass
