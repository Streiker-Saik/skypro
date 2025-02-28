from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transaction_filters import filter_transactions_by_description
from src.transaction_reader import read_csv_transactions, read_excel_transactions
from src.utils import get_transactions_from_json
from src.widget import get_date, mask_account_card


def main() -> None:
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print(
            "Программа: Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON - файла\n"
            "2. Получить информацию о транзакциях из CSV - файла\n"
            "3. Получить информацию о транзакциях из XLSX - файла)"
        )
        user_input = input("Пользователь: ")
        if user_input == "1":
            transactions = get_transactions_from_json("data/operations.json")
            print("Программа: Для обработки выбран JSON-файл.")
            break
        elif user_input == "2":
            transactions = read_csv_transactions("data/transactions.csv")
            print("Программа: Для обработки выбран CSV-файл.")
            break
        elif user_input == "3":
            transactions = read_excel_transactions("data/transactions_excel.xlsx")
            print("Программа: Для обработки выбран XLSX-файл.")
            break
        else:
            print(f"{user_input} - варианта нет")

    while True:
        print(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_input = input("Пользователь: ")
        if user_input.upper() in ("EXECUTED", "CANCELED", "PENDING"):
            transactions = filter_by_state(transactions, user_input.upper())
            print(f"Программа: Операции отфильтрованы по статусу '{user_input.upper()}'")
            break
        else:
            print(f"Программа: Статус операции '{user_input}' недоступен")

    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        user_input = input("Пользователь: ")
        if user_input.title() == "Да":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            user_input = input("Пользователь: ")
            if user_input.lower() == "по возрастанию":
                transactions = sort_by_date(transactions, True)
                break
            elif user_input.lower() == "по убыванию":
                transactions = sort_by_date(transactions)
                break
            else:
                print(f"{user_input} - ответ не корректный")
        elif user_input.title() == "Нет":
            break
        else:
            print(f"{user_input} - ответ не корректный")

    while True:
        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        user_input = input("Пользователь: ")
        if user_input.title() == "Да":
            transactions = list(filter_by_currency(transactions, "RUB"))
            break
        elif user_input.title() == "Нет":
            break
        else:
            print(f"{user_input} - ответ не корректный")

    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input("Пользователь: ")
        if user_input.title() == "Да":
            user_search_string = input("Пользователь(введите слово): ")
            transactions = filter_transactions_by_description(transactions, user_search_string)
            break
        elif user_input.title() == "Нет":
            break
        else:
            print(f"{user_input} - ответ не корректный")

    print("Программа: Распечатываю итоговый список транзакций...")
    if not transactions:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    else:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            print(f"\n{get_date(transaction.get("date", ""))} {transaction.get("description", "")}")
            if "from" in transaction:
                print(
                    f"{mask_account_card(transaction.get('to', ''))} ->"
                    f" {mask_account_card(transaction.get('from', ''))}"
                )
            else:
                print(mask_account_card(transaction.get("to", "")))
            print(
                f"Сумма: {transaction.get('operationAmount', '').get('amount', '')} "
                f"{transaction.get('operationAmount', '').get('currency', '').get('name', '')}"
            )
    return


if __name__ == "__main__":
    main()
