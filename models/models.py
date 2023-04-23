from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# модель для анализа злобности
classifier = pipeline("sentiment-analysis")

# загрузка модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")


def get_models():
    return classifier, tokenizer, model
