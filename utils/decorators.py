import traceback

from datetime import datetime as dt
from typing import Any, Callable

from utils.logger import Logger


def log(logger: Logger, message: str) -> Any:
    """Фабрика декоратора (для подачи в него аршументов)

    Args:
        function (Callable): функция, которую декорируем
        logger (Logger): объект логгера
        message (str): сообщение, которое записываем в лог

    Returns:
        Any: результат функции
    """
    def decorator(function: Callable) -> Any:
        """Декоратор, замеряющий время и обрабатывающий ошибки

        Returns:
            Any: результат функции
        """
        def wrapper(*args, **kwargs) -> Any:
            """Враппер для декоратора

            Returns:
                Any: результат функции, которую декорируем
            """
            returned_value = None
            try:
                start_time = dt.now()
                returned_value = function(*args, **kwargs)
                logger.write(message, "info", (dt.now() - start_time).total_seconds())
            except Exception as err:
                logger.write_error(f"{err}\n{traceback.format_exc()}")
            return returned_value
        return wrapper
    return decorator
