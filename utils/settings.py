import tempfile
from os import path as osp

# Настройки для приложения
settings = {
    "MAX_HISTORY_LEN": 1000,
    "MAX_ANSWER_LEN": 50,
    "LOG_PATH": osp.join(tempfile.gettempdir, "streamlit_chat_logs")
}
