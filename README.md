# Проект "Банковское приложение"

## Описание:

Проект "Банковское приложение" - это приложение на Python

## Проверить версию Python:

Убедитесь, что у вас установлен Python (версия 3.x). Вы можете проверить установленную версию Python, выполнив команду:
```
python --version
```

## Установка Poerty:
Если у вас еще не установлен Poetry, вы можете установить его, выполнив следующую команду
```
curl -sSL https://install.python-poetry.org | python3 -
```
Проверить Poetry добавлен в ваш PATH.
```
poetry --version
```

## Установка:
1. Клонируйте репозиторий:
```
git clone git@github.com:Streiker-Saik/skypro.git
```
2. Перейдите в директорию проекта:
```
cd ваш-репозиторий
```
3. Установите необходимые зависимости:
```
poetry add pip 
poetry add --group lint flack8 black isort mypy
```

## Примеры работы функций:

Модуль src.masks.py
```
print(get_mask_card_number(1596837868705199))
1596 83** **** 5199

print(get_mask_account(64686473678894779589))
**9589
```

Модуль src.widget.py
```
print(mask_account_card("Maestro 1596837868705199"))
Maestro 1596 83** **** 5199
print(mask_account_card("Счет 64686473678894779589"))
Счет **9589

print(get_date("2018-06-30T02:08:58.425572"))
30.06.2018
```

Модуль src.processing.py
```
user_id_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(user_id_list))
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

print(filter_by_state(user_id_list, "CANCELED"))
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(sort_by_date(user_id_list))
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
