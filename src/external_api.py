import datetime
import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

# def transaction_total_amount_in_rub(transactions: List[Dict[str, Any]]) -> float:
#     """Функция, принимает транзакции, выводит сумму транзакций в рублях. С конвертацией на сегодняшний день"""
#     code = "RUB"
#     transactions_amount = []
#     transactions_currency_amount = {}
#
#     for transaction in transactions:
#         # {
#         #     "id": 441945886,
#         #     "state": "EXECUTED",
#         #     "date": "2019-08-26T10:50:58.294041",
#         #     "operationAmount": {
#         #         "amount": "31957.58",
#         #         "currency": {
#         #             "name": "руб.",
#         #             "code": "RUB"
#         #         }
#         #     },
#         #     "description": "Перевод организации",
#         #     "from": "Maestro 1596837868705199",
#         #     "to": "Счет 64686473678894779589"
#         # }
#         code_currency = transaction["operationAmount"]["currency"]["code"]
#         amount = float(transaction["operationAmount"]["amount"])
#
#         if code_currency not in transactions_currency_amount:
#             transactions_currency_amount[code_currency] = amount
#         else:
#             transactions_currency_amount[code_currency] += amount
#
#     for key, values in transactions_currency_amount.items():
#         if key == code:
#             transactions_amount.append(round(values, 2))
#         else:
#             convert_rates = get_apilayer_convert_rates(code_to=code, code_from=key, amount=str(round(values, 2)))
#             transactions_amount.append(convert_rates)
#
#     return sum(transactions_amount)


def get_apilayer_convert_rates(date: Optional[str] = None, *, code_to: str, code_from: str, amount: str) -> float:
    """Функция конвертации валюты, Exchange Rates Data API: https://apilayer.com/marketplace/exchangerates_data-api"""
    load_dotenv("../.env")
    api_key = os.getenv("APILAYER_EDAPI_KEY")

    payload: Dict[Any, Any] = {}
    headers = {"apikey": api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_to}&from={code_from}&amount={amount}"
    if date:
        url += f"&date={date}"

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text

        if response.status_code != 200:
            raise Exception(f"Ошибка API: {status_code} - {result}")

        output_data = response.json()
        return round(float(output_data["result"]), 2)

    except requests.exceptions.ConnectionError:
        raise Exception("Connection Error. Please check your network connection")

    except Exception as exc_info:
        raise Exception(f"Что-то пошло не так. {str(exc_info)}")


def transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """Функция, принимает транзакции, выводит сумму транзакции в рублях"""
    code = "RUB"
    try:
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
        amount = transaction["operationAmount"]["amount"]
        date_string = transaction["date"]
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
        # YYYY-MM-DD
        date = date_obj.strftime("%Y-%m-%d")
        if code_currency == "RUB":
            result = round(float(amount), 2)
        else:
            result = get_apilayer_convert_rates(date, code_to=code, code_from=code_currency, amount=amount)
        return result

    except KeyError as ext_info:
        raise ValueError(f"Ключ не найден: {ext_info}")


# from src.utils import get_transactions_from_json
# if __name__ == "__main__":
#     print(get_apilayer_convert_rates("2000-01-01", code_to="RUB", code_from="USD", amount="1"))
#     transactions = get_transactions_from_json("operations.json")
#     count = 0
#     for transaction in transactions:
#         count += 1
#         print(transaction_amount_in_rub(transaction))
#         if count == 2:
#             break
#     result =transaction_total_amount_in_rub(transactions)
#     print(result)
