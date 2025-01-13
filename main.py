from src.masks import get_mask_account, get_mask_card_number

while True:
    try:
        card_number = int(input("Ввведите номер карты: "))
    except ValueError:
        print("ОШИБКА: Номер карты должен состоять из цифр, попробуйту еще")
    else:
        if len(str(card_number)) == 16:
            break
        else:
            print("Номер карты состоит из 16 цифр")

while True:
    try:
        account_number = int(input("Ввведите номер счета: "))
    except ValueError:
        print("ОШИБКА: Номер счета состоять из цифр, попробуйту еще")
    else:
        if len(str(account_number)) == 20:
            break
        else:
            print("Номер счета состоит из 20 цифр")

mask_card_number = get_mask_card_number(card_number)
mask_account = get_mask_account(account_number)

print(mask_card_number)
print(mask_account)
