import re

from collections import Counter
from typing import Any, Dict, List


# функцию, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
# а возвращать список словарей, у которых в описании есть данная строка
def filter_transactions_by_description(transactions_list: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    pass


# функцию, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
# а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
def count_transactions_by_category(transactions_list: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    pass