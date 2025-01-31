from typing import Tuple

import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(input_account_card: Tuple[str, str]) -> None:
    account_card, conclusion = input_account_card
    """
    Функция проверяет, правильно ли функция mask_account_card обрабатывает различные
    типы входных данных (например, карты и счета)
    Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
    Обрабатывает некорректные входные данные, такие как None и целое число. В этих случаях
    должны возникать исключения TypeError с соответствующими сообщениями.
    """
    with pytest.raises(TypeError) as exc_info:
        mask_account_card(None)
    assert str(exc_info.value) == "Вводные дынные отсутствуют"

    with pytest.raises(TypeError) as exc_info:
        mask_account_card(1)
    assert str(exc_info.value) == "Введено не строковое значение"

    assert mask_account_card(account_card) == conclusion


def test_get_date(data: str) -> None:
    """
    Функция проверяет, правильно ли функция get_date обрабатывает даты.
    Проверка работы функции на различных входных форматах даты, включая граничные случаи
    и нестандартные строки с датами.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата
    """
    with pytest.raises(TypeError) as exc_info:
        get_date(None)
    assert str(exc_info.value) == "Вводные дынные отсутствуют"

    with pytest.raises(TypeError) as exc_info:
        get_date(1)
    assert str(exc_info.value) == "Введено не строковое значение"

    with pytest.raises(ValueError) as exc_value_info:
        get_date("2024-13-11T02:26:18.671407")
    assert str(exc_value_info.value) == "Вводные дынные некорректны"

    assert get_date(data) == "11.03.2024"
