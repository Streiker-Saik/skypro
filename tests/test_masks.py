from typing import Any, Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: Union[int, str]) -> None:
    """Тестирование правильности маскирования номера карты"""

    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (None, "Вводные дынные отсутствуют"),
        ([], "Введен не корректный тип данных"),
        (
            123,
            "В номере карты должно быть 16 цифр",
        ),
    ],
)
def test_get_mask_card_number_crash(card_number: Union[int, Any], expected: str) -> None:
    """
    Тестирование работы функции на различных входных форматах номеров карт,
    включая граничные случаи и нестандартные длины номеров.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
    """

    with pytest.raises(Exception) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == expected


def test_get_mask_account(account_number: Union[int, str]) -> None:
    """Тестирование правильности маскирования номера счета."""

    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (None, "Вводные дынные отсутствуют"),
        ([], "Введен не корректный тип данных"),
        (
            1234,
            "В номере счета должно быть 20 цифр",
        ),
    ],
)
def test_get_mask_account_crash(account_number: Union[int, Any], expected: str) -> None:
    """
    Тестирование работы функции с различными форматами и длинами номеров счетов.
    Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
    """

    with pytest.raises(Exception) as exc_info:
        get_mask_account(account_number)
    assert str(exc_info.value) == expected
