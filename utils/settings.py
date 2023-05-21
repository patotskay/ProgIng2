import tempfile
from os import path as osp
import os
from pathlib import Path

from utils.logger import Logger

# Настройки для приложения
settings = {
    "MAX_HISTORY_LEN": 1000,
    "MAX_ANSWER_LEN": 50,
    "LOG_PATH": osp.join(tempfile.gettempdir(), "streamlit_chat_logs"),
    "SCRIPT_PATH": Path(os.path.realpath(__file__)).parent.parent,
    "MODEL": "our"
}

logger = Logger(settings['LOG_PATH'])
