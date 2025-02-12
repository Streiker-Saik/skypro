from typing import Any

import pytest

from src.decorators import log
from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "argument, expected",
    [
        (7000792289606361, "get_mask_card_number ok.\n"),
        (None, "get_mask_card_number error: TypeError: Вводные дынные отсутствуют. Inputs: (None,), {}.\n"),
        ("", "get_mask_card_number error: TypeError: Введено не числовое значение. Inputs: ('',), {}.\n"),
        (
            70007922896063611,
            "get_mask_card_number error: ValueError: В номере карты должно быть 16 цифр. Inputs: (70007922896063611,), {}.\n",
        ),
    ],
)
def test_log_get_mask_card_number(capsys: pytest.CaptureFixture, argument: Any, expected: str) -> None:
    """Тестирование работы декоратора 'log', на разные данные функции 'get_mask_card_number'"""

    decoder_get_mask_card_number = log(None)(get_mask_card_number)

    decoder_get_mask_card_number(argument)
    captured = capsys.readouterr()
    assert (expected) in captured.out
