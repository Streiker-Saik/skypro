import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, conclusion",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_card, conclusion):
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


def test_get_date(data):
    """

    Тестирование правильности преобразования даты.
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

    with pytest.raises(ValueError) as exc_info:
        get_date("2024-13-11T02:26:18.671407")
    assert str(exc_info.value) == "Вводные дынные некорректны"

    assert get_date(data) == "11.03.2024"
