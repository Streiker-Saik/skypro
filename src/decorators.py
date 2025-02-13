import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None, directory: str = "data") -> Callable:
    """"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                func(*args, **kwargs)
                message = f"{func.__name__} ok."

            except TypeError as error_message:
                message = f"{func.__name__} error: TypeError: {error_message}. Inputs: {args}, {kwargs}."

            except ValueError as error_message:
                message = f"{func.__name__} error: ValueError: {error_message}. Inputs: {args}, {kwargs}."

            # другие не учтенные ошибки
            # except Exception as error_message:
            #     message = f"{func.__name__} error: Exception: {error_message}. Inputs: {args}, {kwargs}."

            if not filename:
                print(message)
            else:
                os.chdir("..")
                # проверка на существовании директории, при отсутствии, создается.
                if not os.path.exists(directory):
                    os.makedirs(directory)

                with open(os.path.join(directory, filename), "a", encoding="utf-8") as file:
                    file.write(f"{message}\n")

            # return result

        return wrapper

    return decorator
