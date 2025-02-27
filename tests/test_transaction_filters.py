from typing import Any, Dict, List

import pytest

from src.transaction_filters import count_transactions_by_description, filter_transactions_by_description


@pytest.mark.parametrize(
    "search_string, expected",
    [
        (
            "со счета на счет",
            [
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
            ],
        ),
        (
            "организации",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
        (
            "с карты на карту",
            [
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                }
            ],
        ),
        (
            "неизвестно",
            [],
        ),
    ],
)
def test_filter_transactions_by_description(
    transactions: List[Dict[str, Any]], search_string: str, expected: List[Dict[str, Any]]
) -> None:
    assert filter_transactions_by_description(transactions, search_string) == expected


def test_count_transactions_by_description(transactions: List[Dict[str, Any]]) -> None:
    count_description = {
        "Перевод со счета на счет": 0,
        "Перевод организации": 0,
        "Перевод с карты на карту": 0,
        "Неизвестно": 0,
    }
    assert count_transactions_by_description(transactions, count_description) == {
        "Перевод со счета на счет": 2,
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
        "Неизвестно": 0,
    }
