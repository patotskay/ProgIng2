from utils.settings import settings
# текстовый контент на русском языке

if settings['MODEL'] == 'our':
    MAIN_TITLE = "Чат-бот, который умеет в арифметику"
    SUB_TITLE = "Введите свой запрос (арифметическая задачка, помнит 4 шага). Например, y=2x -> (после ответа) "
    SUB_TITLE += "прибавь к результату 2. Учился на датасете Сбера (или не Сбреа, по профилю не понятно), "
    SUB_TITLE += "моделька DialoGPT (подробно в репозитории в тетрадке ./reseach)"
else:
    MAIN_TITLE = "Чат-бот на основе DialoGPT-medium"
    SUB_TITLE = "Введите свой запрос и получите ответ от чат-бота на основе модели DialoGPT-medium от Microsoft:"


def get_text_content():
    return MAIN_TITLE, SUB_TITLE
