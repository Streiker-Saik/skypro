from typing import Any, Dict, List, Tuple

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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
    """Генератор не завершается ошибкой при обработке пустого списка или
    списка без соответствующих валютных операций"""
    result = list(filter_by_currency([], "EUR"))
    assert result == []


# Проверьте, что функция возвращает корректные описания для каждой транзакции.
# Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
def test_transaction_descriptions():
    pass


@pytest.mark.parametrize(
    "start_generator, stop_generator, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (10001, 10003, ["0000 0000 0001 0001", "0000 0000 0001 0002", "0000 0000 0001 0003"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start_generator: int, stop_generator: int, expected: str) -> None:
    """Тестирование, что функция правильно выдает номера карт в заданном диапазоне,
    корректность форматирования номеров карт и корректно обрабатывает крайние значения"""
    assert card_number_generator(start_generator, stop_generator) == expected


@pytest.mark.parametrize("start_generator, stop_generator", [("1", 3), (1, "3")])
def test_card_number_wrong_type(start_generator: Any, stop_generator: Any) -> None:
    """Функция проверяет на корректные вводные данные"""
    with pytest.raises(TypeError) as exc_info:
        card_number_generator(start_generator, stop_generator)
        assert str(exc_info.value) == "Введено не числовое значение"


def test_card_number_not_correct_input() -> None:
    """Функция проверяет на вводные данные не входящие в диапазон с 1 до 9999999999999999(16 цифр)"""
    with pytest.raises(ValueError) as exc_info:
        card_number_generator(0, 1)
        assert str(exc_info.value) == "Введены числа не в диапазоне с 1 до 9999999999999999(16 цифр)"
