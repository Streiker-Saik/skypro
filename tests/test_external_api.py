import os
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.external_api import get_apilayer_convert_rates, transaction_amount_in_rub


def test_transaction_amount_in_rub_rub() -> None:
    """Тестирование при валюте в 'RUB'"""
    transaction = {
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
    assert transaction_amount_in_rub(transaction) == 31957.58


def test_transaction_amount_in_rub_none_key() -> None:
    """Тестирование если ключ в словаре отсутствует"""
    with pytest.raises(ValueError) as exc_info:
        transaction = {
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                },
            }
        }
        transaction_amount_in_rub(transaction)
        assert str(exc_info.value) == "Ключ не найден: 'code'"


@patch("src.external_api.get_apilayer_convert_rates")
def test_transaction_amount_in_rub_usd(mock_get: MagicMock) -> None:
    """Тестирование при валюте в 'USD'"""
    transaction = {
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }

    mock_get.return_value = 520543.42
    result = transaction_amount_in_rub(transaction)
    assert result == 520543.42


@patch("requests.request")
def test_get_apilayer_convert_rates(mock_request: MagicMock) -> None:
    """Тестирование, правильно ли функция возвращает при успешном запросе"""
    code_to = "RUB"
    code_from = "USD"
    amount = "1"
    expected_result = 88.95

    mock_request.return_value.json.return_value = {"result": expected_result}
    mock_request.return_value.status_code = 200

    assert get_apilayer_convert_rates(code_to=code_to, code_from=code_from, amount=amount) == expected_result

    api_key = os.getenv("APILAYER_EDAPI_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}"
    mock_request.assert_called_once_with("GET", url, headers={"apikey": api_key}, data={})


@patch("requests.request")
def test_get_apilayer_convert_rates_api_error(mock_request: MagicMock) -> None:
    """Тестирование, правильно ли функция обрабатывает ошибки"""
    code_to = "RUB"
    code_from = "USD"
    amount = "1"

    mock_request.return_value.status_code = 429
    mock_request.return_value.text = "You have"

    with pytest.raises(Exception) as exc_info:
        get_apilayer_convert_rates(code_to=code_to, code_from=code_from, amount=amount)

    assert "Что-то пошло не так. Ошибка API: 429 - You have" in str(exc_info)


@patch("requests.request")
def test_get_apilayer_convert_rates_connection_error(mock_request: MagicMock) -> None:
    """Тестирование, правильно ли функция обрабатывает ошибку соединения"""
    code_to = "RUB"
    code_from = "USD"
    amount = "1"

    # имитация ошибки соединения
    mock_request.side_effect = requests.exceptions.ConnectionError

    with pytest.raises(Exception) as exc_info:
        get_apilayer_convert_rates(code_to=code_to, code_from=code_from, amount=amount)

    assert "Connection Error. Please check your network connection" in str(exc_info)


@patch("requests.request")
def test_get_apilayer_convert_rates_introduction_date(mock_request: MagicMock) -> None:
    """Тестирование, правильно ли функция возвращает при успешном запросе"""
    code_to = "RUB"
    code_from = "USD"
    amount = "1"
    date = "2000-01-01"
    expected_result = 27.48

    mock_request.return_value.json.return_value = {"result": expected_result}
    mock_request.return_value.status_code = 200

    assert get_apilayer_convert_rates(date, code_to=code_to, code_from=code_from, amount=amount) == expected_result

    api_key = os.getenv("APILAYER_EDAPI_KEY")
    url = (
        f"https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}"
        f"&date={date}"
    )
    mock_request.assert_called_once_with("GET", url, headers={"apikey": api_key}, data={})
