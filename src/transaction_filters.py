import re
from collections import Counter
from typing import Any, Dict, List


def filter_transactions_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция принимает транзакции и строку поиска, выводит список транзакций у которых есть данная строка"""
    # return [transaction for transaction in transactions if transaction["description"] == search_string]
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


# def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
#     """Функция принимает транзакции и список категорий, выводит подсчет транзакций в этих категориях"""
#     transactions_by_category = {}
#     for transaction in transactions:
#         description = transaction.get("description")
#         if description in categories:
#             if description in transactions_by_category:
#                 transactions_by_category[description] += 1
#             else:
#                 transactions_by_category[description] = 1
#     return transactions_by_category


def count_transactions_by_description(
    transactions: List[Dict[str, Any]], count_dict: Dict[str, int]
) -> Dict[str, int]:
    """Функция принимает транзакции и словарь для подсчета, выводит обновленный словарь"""
    # descriptions = []
    # for transaction in transactions:
    #     descriptions.append(transaction.get("description"))
    descriptions = [transaction.get("description", "") for transaction in transactions]
    count_descriptions = Counter(descriptions)
    # for item, count in count_descriptions.items():
    #     count_dict[item] = count
    count_dict.update(count_descriptions)
    return count_dict


# if __name__ == "__main__":
#     from src.utils import get_transactions_from_json
#     transactions = get_transactions_from_json("../data/operations.json")
#     print(filter_transactions_by_description(transactions, 'Открытие'))
#     # {'Перевод организации': 40, 'Перевод с карты на карту': 19, 'Перевод с карты на счет': 16,
#     #  'Перевод со счета на счет': 15, 'Открытие вклада': 10}
#     print(count_transactions_by_description(transactions, {"неизвестно": 0}))
