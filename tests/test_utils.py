import json
import os
from typing import Any, Dict, List

import pytest

from src.utils import get_transactions_from_json


def test_get_transactions_from_json_non_existent_file() -> None:
    """Тест, если файл не найден"""
    assert get_transactions_from_json("non.json") == []


@pytest.fixture
def transactions_from_to() -> List[Dict[str, Any]]:
    return [
        {"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}},
        {"operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}},
        {"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}},
    ]
def test_get_transactions_from_json(transactions_from_to: List[Dict[str, Any]]) -> None:
    """Тест работы функции"""
    file_path = "../data/test.json"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            json.dump(transactions_from_to, file_json, indent=4, ensure_ascii=False)

        assert get_transactions_from_json(file_path) == transactions_from_to
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_get_transactions_from_json_empty_list() -> None:
    """Тест, если файл с пустым списком"""
    file_path = "../data/test.json"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            transactions_from_to: List = []
            json.dump(transactions_from_to, file_json, indent=4, ensure_ascii=False)

        assert get_transactions_from_json(file_path) == transactions_from_to
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_get_transactions_from_invalid_json() -> None:
    """Тест, если файл с некорректными данными"""
    file_path = "../data/test.json"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            transactions_from_to = "некорректные данные"
            file_json.write(transactions_from_to)

        assert get_transactions_from_json(file_path) == []
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_get_transactions_from_json_not_list() -> None:
    """Тест, если файл не со списком"""
    file_path = "../data/test.json"
    try:
        with open(file_path, "w", encoding="utf-8") as file_json:
            transactions_from_to: str = ""
            json.dump(transactions_from_to, file_json, indent=4, ensure_ascii=False)

        assert get_transactions_from_json(file_path) == []
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
