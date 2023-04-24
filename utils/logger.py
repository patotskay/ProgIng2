from datetime import datetime as dt
from os import path as osp


class Logger:

    def __init__(self, base_path: str) -> None:
        """Инициализация

        Args:
            base_path (str): путь до папки логов
        """

        self.log_file = osp.join(base_path, f"{dt.now().strftime('%d.%m.%y-%H:%M')}_log")
        self.error_file = osp.join(base_path, f"{dt.now().strftime('%d.%m.%y-%H:%M')}_errors")
        self.error_id = 0

        open(self.log_file, "w").close()
        open(self.error_file, "w").close()

    def write(self, message: str, status: str) -> None:
        """Запись в лог

        Args:
            message (str): текстовое сообщение
            status (str): один из статусов - "I" (info), "W" (warning), "E" (error)
        """
        with open(self.log_file, "a") as f:
            f.write(f"[{status} {dt.now().strftime('%d.%m.%y %H:%M:%S')} {message}\n")

    def write_error(self, traceback: str) -> None:
        """Запись ошибок

        Args:
            traceback (str): traceback ошибки
        """

        with open(self.log_file, "a") as f:
            f.write(f"[E {dt.now().strftime('%d.%m.%y %H:%M:%S')} Server has error in runtime [id: {self.error_id}]")

        with open(self.error_file, "a") as f:
            f.write(f"[id: {self.error_id}]\n{traceback}\n\n")
