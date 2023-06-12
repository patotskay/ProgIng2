import os
from typing import Union
import torch
from transformers import pipeline
from transformers import AutoModelWithLMHead, AutoTokenizer

from utils.decorators import log
from utils.settings import settings, logger


@log(logger=logger, message="Модели загружены")
def get_models():
    # модель для анализа злобности
    classifier = pipeline("sentiment-analysis")

    # загрузка модели и токенизатора
    tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
    model = AutoModelWithLMHead.from_pretrained(os.path.join(settings['SCRIPT_PATH'], 'our_gpt/content/output-small'))
    return classifier, tokenizer, model


classifier, tokenizer, model = get_models()


@log(logger=logger, message="Ответ получен")
def get_answer(user_input: str, prev_phrase: Union[torch.Tensor, None] = None, step: int = 0) -> str:
    """Получение ответа от модели

    Args:
        user_input (str): строка запроса от пользователя
        prev_phrase (torch.Tensor): для контекста (прошлый отклик модели)
        step (int): шаг контекста

    Returns:
        str: ответ модели
    """
    global classifier
    global tokenizer
    global model

    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([prev_phrase, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=100,
        top_p=0.7,
        temperature=0.8,
    )

    return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)


@log(logger=logger, message="Анализ агресивности произведен")
def get_toxic(user_input):
    return classifier(user_input)[0]['label']
