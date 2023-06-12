from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from utils.decorators import log
from utils.settings import settings, logger


@log(logger=logger, message="Модели загружены")
def get_models():
    # модель для анализа злобности
    classifier = pipeline("sentiment-analysis")

    # загрузка модели и токенизатора
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
    return classifier, tokenizer, model


classifier, tokenizer, model = get_models()


@log(logger=logger, message="Ответ получен")
def get_answer(user_input: str) -> str:
    """Получение ответа от модели

    Args:
        user_input (str): строка запроса от пользователя

    Returns:
        str: ответ модели
    """
    global classifier
    global tokenizer
    global model

    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(
        input_ids, max_length=settings['MAX_HISTORY_LEN'], pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)


@log(logger=logger, message="Анализ агресивности произведен")
def get_toxic(user_input):
    return classifier(user_input)[0]['label']
