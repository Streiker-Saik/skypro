# from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

card_account_list = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]
date = "2024-03-11T02:26:18.671407"

print(mask_account_card(card_account_list[0]))
print(get_date(date))

# while True:
#     try:
#         card_number = int(input("Ввведите номер карты: "))
#     except ValueError:
#         print("ОШИБКА: Номер карты должен состоять из цифр, попробуйту еще")
#     else:
#         if len(str(card_number)) == 16:
#             break
#         else:
#             print("Номер карты состоит из 16 цифр")
#
# while True:
#     try:
#         account_number = int(input("Ввведите номер счета: "))
#     except ValueError:
#         print("ОШИБКА: Номер счета состоять из цифр, попробуйту еще")
#     else:
#         if len(str(account_number)) == 20:
#             break
#         else:
#             print("Номер счета состоит из 20 цифр")

# mask_card_number = get_mask_card_number(card_number)
# mask_account = get_mask_account(account_number)

# print(mask_card_number)
# print(mask_account)
