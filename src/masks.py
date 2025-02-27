import logging
import os
from typing import Union

# создание абсолютного пути из относительного
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
log_file = os.path.join(project_root, 'logs', 'masks.log')

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: XXXX XX** **** XXXX"""

    if card_number is None:
        error_message = "Вводные дынные отсутствуют"
        masks_logger.error(error_message)
        raise TypeError(error_message)

    if not isinstance(card_number, (int, str)):
        error_message = "Введен не корректный тип данных"
        masks_logger.error(error_message)
        raise TypeError(error_message)

    masks_logger.info(f"Выполняем маскировку номера карты {card_number}")
    card_number_string = str(card_number)

    if len(card_number_string) != 16 or not card_number_string.isdigit():
        error_message = "В номере карты должно быть 16 цифр"
        masks_logger.error(error_message)
        raise ValueError(error_message)

    result = f"{card_number_string[-16:-12]} {card_number_string[-12:-10]}** **** {card_number_string[-4:]}"
    masks_logger.info("Маскировка карты - прошло успешно")
    return result


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция переводит целое число в строку и записывает через f строку со срезом: **XXXX"""

    if account_number is None:
        error_message = "Вводные дынные отсутствуют"
        masks_logger.error(error_message)
        raise TypeError(error_message)

    if not isinstance(account_number, (int, str)):
        error_message = "Введен не корректный тип данных"
        masks_logger.error(error_message)
        raise TypeError(error_message)

    masks_logger.info(f"Выполняем маскировку номера счета {account_number}")
    account_number_string = str(account_number)

    if len(account_number_string) != 20 or not account_number_string.isdigit():
        error_message = "В номере счета должно быть 20 цифр"
        masks_logger.error(error_message)
        raise ValueError(error_message)

    result = f"**{account_number_string[-4:]}"
    masks_logger.info("Маскировка счета - прошло успешно")
    return result
