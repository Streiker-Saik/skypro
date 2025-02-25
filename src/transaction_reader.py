from typing import Any, Dict, List, cast

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция принимает файл (*.csv) и выводит список словарей"""
    try:
        transactions_df = pd.read_csv(file_path, delimiter=";")
        transactions_list = transactions_df.to_dict(orient="records")
        return cast(List[Dict[str, Any]], transactions_list)
        # return pd.read_csv(file_path, delimiter=";").to_dict(orient="records")

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл по пути: {file_path} - не найдет")


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция принимает файл (*.xlsx) и выводит список словарей"""
    try:
        transactions_df = pd.read_excel(file_path)
        transactions_list = transactions_df.to_dict(orient="records")
        return cast(List[Dict[str, Any]], transactions_list)
        # return pd.read_excel(file_path).to_dict(orient="records")

    except FileNotFoundError:
        raise FileNotFoundError(f"Файл по пути: {file_path} - не найдет")


# if __name__ == "__main__":
#     print(read_csv_transactions("../data/transactions.csv")[0:2])
#     print(read_excel_transactions("../data/transactions_excel.xlsx")[0:2])
