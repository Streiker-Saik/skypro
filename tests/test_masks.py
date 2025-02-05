from typing import Any, Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number: Union[int, Any]) -> None:
    """
    Тестирование правильности маскирования номера карты
    Проверка работы функции на различных входных форматах номеров карт,
    включая граничные случаи и нестандартные длины номеров.
    Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
    """

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number(None)
    assert str(exc_info.value) == "Вводные дынные отсутствуют"

    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Введено не числовое значение"

    with pytest.raises(ValueError) as exc_value_info:
        get_mask_card_number(1)
    assert str(exc_value_info.value) == "В номере карты должно быть 16 цифр"

    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


def test_get_mask_account(account_number: str) -> None:
    """
    Тестирование правильности маскирования номера счета.
    Проверка работы функции с различными форматами и длинами номеров счетов.
    Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
    """

    with pytest.raises(TypeError) as exc_info:
        get_mask_account(None)
    assert str(exc_info.value) == "Вводные дынные отсутствуют"

    with pytest.raises(TypeError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Введено не числовое значение"

    with pytest.raises(ValueError) as exc_value_info:
        get_mask_account(1)
    assert str(exc_value_info.value) == "В номере счета должно быть 20 цифр"

    assert get_mask_account(account_number) == "**4305"
