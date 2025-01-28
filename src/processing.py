def filter_by_state(user_id_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и выводит список по ключу state(по умолчанию EXECUTED)"""
    return [user_id for user_id in user_id_list if user_id["state"] == state]


def sort_by_date(user_id_list: list[dict], ascending: bool = False) -> list[dict]:
    """Функция принимает список словарей и сортирует по ключу date(по умолчанию False - по убыванию)"""
    return sorted(user_id_list, key=lambda user_id: user_id.get("date", 0), reverse=not ascending)
