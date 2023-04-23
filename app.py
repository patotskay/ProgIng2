import streamlit as st
from streamlit.components.v1 import html
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# модель для анализа злобности
classifier = pipeline("sentiment-analysis")

# загрузка модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# задаем параметры генерации ответов
MAX_HISTORY_LEN = 1000
MAX_ANSWER_LEN = 50

# задаем заголовок страницы и описание приложения
TITLE = "Чат-бот на основе DialoGPT-medium"
SUB_TITLE = "Введите свой запрос и получите ответ от чат-бота на основе модели DialoGPT-medium от Microsoft:"

with open("styles.css") as f:
    css = f.read()

# добавляем HTML-блок general-header
with open("templates/general/header.html", "r") as f:
    header = f.read()

html_template = f'<style>{css}</style>\n{header.format(title=TITLE, sub_title=SUB_TITLE)}'
html(html_template, width=800, height=300)

# создаем форму для ввода запросов
user_input = st.text_input("Вы: ")

# если пользователь ввел запрос, обрабатываем его
if user_input:
    # кодируем запрос пользователя и добавляем его в историю чата
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(input_ids, max_length=MAX_HISTORY_LEN, pad_token_id=tokenizer.eos_token_id)

    # декодируем ответ бота и выводим его на страницу
    bot_response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    st.write("Bot: " + bot_response)

# добавляем HTML-блок general-header
with open("templates/main/index.html", "r") as f:
    index = f.read()

label_value = classifier(user_input)[0]['label']

html_template = f'<style>{css}</style>\n{index.format(label=label_value)}'
html(html_template, width=800, height=300)
