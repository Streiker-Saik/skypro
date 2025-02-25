import json
import logging
import os
from typing import Any, Dict, List

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Функцию, принимает на вход путь до JSON-файла и возвращает список словарей с данными убирая пустые словари"""
    if not os.path.exists(file_path):
        utils_logger.error(f'Файл "{file_path}" - не найден')
        return []

    try:
        utils_logger.info(f'Выполняем преобразование JSON-файла "{file_path}" в объект Python')
        with open(file_path, "r", encoding="utf-8") as json_file:
            transactions: List[Dict[str, Any]] = json.load(json_file)

            if type(transactions) is not list:
                utils_logger.error("Файл содержит не список")
                return []

            # убираем пустые словари
            result = list(filter(bool, transactions))
            utils_logger.info(f'Преобразование JSON-файла "{file_path}" в объект Python выполнено')
            return result

    except json.JSONDecodeError as exc_info:
        utils_logger.error(f"Невозможно преобразовать json дынные: {exc_info}")
        return []


# if __name__ == "__main__":
#     print(get_transactions_from_json("../data/operations.json"))
