import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None, directory: str = "data") -> Callable:
    """Декоратор выводящий логи выполнение функций, в файл(по умолчанию на консоль) в директорию (по умолчанию data)"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            message = ""
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok."
                return result

            except Exception as error_message:
                message = (
                    f"{func.__name__} error: {error_message.__class__.__name__}: "
                    f"{error_message}. Inputs: {args}, {kwargs}."
                )

            finally:
                if not filename:
                    print(message)
                else:
                    os.chdir("..")  # в данных расположениях выходит в директорию выше, далее скорректировать
                    # проверка на существовании директории, при отсутствии, создается.
                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    with open(os.path.join(directory, filename), "a", encoding="utf-8") as file:
                        file.write(f"{message}\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator
