# import json
# import os
# from typing import Any, Dict, List
#
# import requests
# from dotenv import load_dotenv
# from unittest.mock import patch
# from src.external_api import transaction_amount_in_rub, get_apilayer_convert_rates
#
#
# def test_transaction_amount_in_rub():
#     pass
#
#
# @patch("requests.request")
# def test_get_apilayer_convert_rates(mock_get):
#     mock_get.return_value.json.return_value = {"result": 1}
#     assert get_apilayer_convert_rates(code_to="RUB", code_from="USD", amount="1") == 1
#     # load_dotenv("../.env")
#     # apikey_ = os.getenv("APILAYER_EDAPI_KEY")
#     # payload: Dict[Any, Any] = {}
#     # headers = {"apikey": apikey_}
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
#     requests.request("GET", url, headers=headers, data=payload)
#
#     # status_code = response.status_code
#     # result = response.text
#     # output_data = json.loads(result)
#     # mock_get.assert_called_once_with(response)
