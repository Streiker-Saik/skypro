from src.processing import filter_by_state, sort_by_date
from typing import List, Tuple, Dict, Any


def test_filter_by_state(input_state: Tuple[List[Dict[str, Any]], str, List[Dict[str, Any]]]) -> None:
    input_list, state, conclusion = input_state
    """
    Тестирование фильтрации списка словарей по заданному статусу state.
    Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
    Параметризация тестов для различных возможных значений статуса state.
    """
    assert filter_by_state(input_list, state) == conclusion


def test_sort_by_date(input_date: Tuple[List[Dict[str, Any]], bool, List[Dict[str, Any]]]) -> None:
    input_list, ascending, conclusion = input_date
    """
    Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
    Проверка корректности сортировки при одинаковых датах.
    """
    assert sort_by_date(input_list, ascending) == conclusion
