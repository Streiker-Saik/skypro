import json
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

# from src.utils import get_transactions_from_json


def transaction_amount_in_rub(transactions: List[Dict[str, Any]], code: str = "RUB") -> float:
    """Функция, принимает транзакции, выводит сумму транзакций в рублях"""
    transactions_amount = []
    transactions_currency = {}

    for transaction in transactions:
        # {
        #     "id": 441945886,
        #     "state": "EXECUTED",
        #     "date": "2019-08-26T10:50:58.294041",
        #     "operationAmount": {
        #         "amount": "31957.58",
        #         "currency": {
        #             "name": "руб.",
        #             "code": "RUB"
        #         }
        #     },
        #     "description": "Перевод организации",
        #     "from": "Maestro 1596837868705199",
        #     "to": "Счет 64686473678894779589"
        # }
        code_currency = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])

        if code_currency not in transactions_currency:
            transactions_currency[f"{code_currency}"] = amount
        else:
            transactions_currency[f"{code_currency}"] += amount

    for key, values in transactions_currency.items():
        if key == code:
            transactions_amount.append(round(values, 2))
        else:
            convert_rates = get_apilayer_convert_rates(code_to=code, code_from=key, amount=str(round(values, 2)))
            transactions_amount.append(convert_rates)

    return sum(transactions_amount)


def get_apilayer_convert_rates(*, code_to: str, code_from: str, amount: str) -> float:
    """Функция конвертации валюты, Exchange Rates Data API: https://apilayer.com/marketplace/exchangerates_data-api"""
    load_dotenv("../.env")
    apikey_ = os.getenv("APILAYER_EDAPI_KEY")

    payload: Dict[Any, Any] = {}
    headers = {"apikey": apikey_}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}"

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        output_data = json.loads(result)
        return round(float(output_data["result"]), 2)
    except:
        raise Exception(f"Что-то пошло не так. Ошибка {status_code}")


# if __name__ == "__main__":
#     transactions = get_transactions_from_json("operations.json")
#     print(transaction_amount_in_rub(transactions))
