import os
from typing import Any

import pytest

from src.decorators import log
from src.masks import get_mask_card_number


def test_log(capsys: pytest.CaptureFixture) -> None:
    """Тестирование работы функции log"""

    @log()
    def func(x: int) -> int:
        """Тестовая функция умножения"""
        return x * 2

    func(2)
    captured = capsys.readouterr()
    assert "func ok.\n" == captured.out


@pytest.mark.parametrize(
    "argument_log_crash, expected",
    [
        (None, "func error: TypeError: Вводные дынные отсутствуют. Inputs: (None,), {}.\n"),
        ("2", "func error: TypeError: Введено не числовое значение. Inputs: ('2',), {}.\n"),
        (
            -5,
            "func error: ValueError: Число должно быть положительное и не равно 0. Inputs: (-5,), {}.\n",
        ),
    ],
)
def test_func_crash(capsys: pytest.CaptureFixture, argument_log_crash: Any, expected: str) -> None:
    """Тестирование работы функции log при работе с ошибками"""

    @log()
    def func(x: int) -> int:
        """
        Тестовая функция умножения, с проверкой на ошибки:
        вводных данных, числового значения и положительного аргумента
        """
        if x is None:
            raise TypeError("Вводные дынные отсутствуют")
        if not isinstance(x, int):
            raise TypeError("Введено не числовое значение")
        if x <= 0:
            raise ValueError("Число должно быть положительное и не равно 0")
        return x * 2

    with pytest.raises(Exception):
        func(argument_log_crash)

    captured = capsys.readouterr()
    assert expected in captured.out


def test_log_create_and_fill(filename: str = "test.txt", directory: str = "data") -> None:
    """Тестирование функции на создание и заполнение файла в директории"""

    @log(filename)
    def func(x: int) -> int:
        """Тестовая функция умножения"""
        return x * 2

    func(2)
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    with open(filename, "r", encoding="utf-8") as file:
        assert file.readline() == "func ok.\n"
    os.remove(filename)  # удаляем тестовый файл
    os.chdir("..")  # переходим в исходную директорию
    os.rmdir(directory)  # удаляем пустую директорию


def test_log_get_mask_card_number(capsys: pytest.CaptureFixture, card_number: Any) -> None:
    """Тестирование работы декоратора 'log', на разные данные функции 'get_mask_card_number'"""

    decoder_get_mask_card_number = log(None)(get_mask_card_number)
    decoder_get_mask_card_number(card_number)
    captured = capsys.readouterr()
    assert "get_mask_card_number ok.\n" in captured.out


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (None, "get_mask_card_number error: TypeError: Вводные дынные отсутствуют. Inputs: (None,), {}.\n"),
        ([], "get_mask_card_number error: TypeError: Введен не корректный тип данных. Inputs: ([],), {}.\n"),
        (
            70007922896063611,
            "get_mask_card_number error: ValueError: В номере карты должно быть 16 цифр. "
            "Inputs: (70007922896063611,), {}.\n",
        ),
    ],
)
def test_log_get_mask_card_number_crash(capsys: pytest.CaptureFixture, card_number: Any, expected: str) -> None:
    """Тестирование работы декоратора 'log', на разные данные функции 'get_mask_card_number'"""

    decoder_get_mask_card_number = log(None)(get_mask_card_number)
    with pytest.raises(Exception):
        decoder_get_mask_card_number(card_number)
    captured = capsys.readouterr()
    assert expected in captured.out
