import json
import os
from typing import Any, Dict, List


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Функцию, принимает на вход путь до JSON-файла и возвращает список словарей с данными убирая пустые словари"""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            transactions: List[Dict[str, Any]] = json.load(json_file)
            if type(transactions) is not list:
                return []
            # убираем пустые словари
            result = list(filter(bool, transactions))
            return result
    except json.JSONDecodeError:
        return []


# if __name__ == "__main__":
#     print(get_transactions_from_json("../data/operations.json"))
