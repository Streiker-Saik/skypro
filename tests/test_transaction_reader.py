from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.transaction_reader import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(read_csv: MagicMock) -> None:
    """Тестирование, функция возвращает из файла (*.csv) список словарей"""
    read_csv.return_value = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0],
            "state": ["EXECUTED", "EXECUTED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        }
    )
    expected = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
        },
        {"id": 3598919.0, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
    ]
    assert read_csv_transactions("test.csv") == expected


def test_read_csv_transactions_file_none_found() -> None:
    """Тестирование, когда файл не найдет"""
    file_path = "test.csv"

    with pytest.raises(FileNotFoundError) as exc_info:
        read_csv_transactions(file_path)

    assert f"Файл по пути: {file_path} - не найдет" == str(exc_info.value)


@patch("pandas.read_excel")
def test_read_excel_transactions(read_excel: MagicMock) -> None:
    """Тестирование, функция возвращает из файла (*.xlsx) список словарей"""
    read_excel.return_value = pd.DataFrame(
        {
            "id": [650703.0, 3598919.0],
            "state": ["EXECUTED", "EXECUTED"],
            "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        }
    )
    expected = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
        },
        {"id": 3598919.0, "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
    ]
    assert read_excel_transactions("test.xlsx") == expected


def test_read_excel_transactions_file_none_found() -> None:
    """Тестирование, когда файл не найдет"""
    file_path = "test.xlsx"

    with pytest.raises(FileNotFoundError) as exc_info:
        read_excel_transactions(file_path)

    assert f"Файл по пути: {file_path} - не найдет" == str(exc_info.value)
