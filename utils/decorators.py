from datetime import datetime as dt
from functools import wraps

from typing import Any, Callable

from utils.logger import Logger


def log(function: Callable, logger: Logger, message: str) -> Any:
    """Фабрика декоратора (для подачи в него аршументов)

    Args:
        function (Callable): функция, которую декорируем
        logger (Logger): объект логгера
        message (str): сообщение, которое записываем в лог

    Returns:
        Any: результат функции
    """

    @wraps(function)
    def ret_fun(*args, **kwargs) -> Any:
        """Декоратор, замеряющий время и обрабатывающий ошибки

        Returns:
            Any: результат функции
        """
        try:
            start_time = dt.now()
            returned_value = function(*args, **kwargs)
            logger.write(message, "info", (start_time - dt.now().total_seconds()))
        except Exception as err:
            logger.write_error(err.__traceback__)
        return returned_value

    return ret_fun
