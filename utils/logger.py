import os

from datetime import datetime as dt

from pathlib import Path
from os import path as osp


class Logger:

    def __init__(self, base_path: str) -> None:
        """Инициализация

        Args:
            base_path (str): путь до папки логов
        """

        self.log_file = osp.join(base_path, "chat_log")
        self.error_file = osp.join(base_path, "chat_errors")
        self.error_id = 0

        _base_path = Path(base_path)
        if _base_path.stem not in os.listdir(_base_path.parent):
            os.mkdir(base_path)

    def write(self, message: str, status: str, run_time: float) -> None:
        """Запись в лог

        Args:
            message (str): текстовое сообщение
            status (str): один из статусов - "I" (info), "W" (warning), "E" (error)
            run_time (float): время выполнения в секундах
        """

        with open(self.log_file, "a") as f:
            f.write(f"[{status} {dt.now().strftime('%d.%m.%y %H:%M:%S')} {message} ({run_time:.3f})\n")

    def write_error(self, traceback_message: str) -> None:
        """Запись ошибок

        Args:
            traceback (str): traceback ошибки
        """

        with open(self.log_file, "a") as f:
            f.write(f"[E {dt.now().strftime('%d.%m.%y %H:%M:%S')} Server has error in runtime [id: {self.error_id}]")

        with open(self.error_file, "a") as f:
            f.write(f"[id: {self.error_id}]\n{traceback_message}\n\n")

        self.error_id += 1
