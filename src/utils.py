import json
import os
from typing import Any, Dict, List


def get_transactions_from_json(filename: str, directory: str = "data") -> List[Dict[str, Any]]:
    """Функцию, принимает на вход путь до JSON-файла и возвращает список словарей с данными убирая пустые словари"""
    file_path = os.path.join("..", directory, filename)
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            transactions: List[Dict[str, Any]] = json.load(json_file)
            # убираем пустые словари
            result = list(filter(bool, transactions))
            return result
    except json.JSONDecodeError:
        return []


# if __name__ == "__main__":
#     print(get_transactions_from_json("operations.json"))
