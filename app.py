import streamlit as st
from streamlit.components.v1 import html

from models.models import get_models, get_answer
from utils.language.ru import get_text_content

# получим модели
classifier, tokenizer, model = get_models()
# получаем текстовый контент
main_title, sub_title = get_text_content()

# собираем страницу CSS из трех частей HTML:
# 0) добавляем общий файлк с CSS стилями
with open("static/css/styles.css") as f:
    css = f.read()

# 1) HEADER
# добавляем HTML-блок general-header
with open("templates/general/header.html", "r") as f:
    header = f.read()
html_template = f'<style>{css}</style>\n{header.format(title=main_title, sub_title=sub_title)}'
html(html_template, width=800, height=200)

# 2) MAIN
# создаем форму для ввода запросов
user_input = st.text_input("Вы: ")

# если пользователь ввел запрос, обрабатываем его
if user_input:
    # кодируем запрос пользователя и добавляем его в историю чата
    bot_response = get_answer(user_input)
    st.write("Bot: " + bot_response)

# добавляем HTML-блок general-header
with open("templates/main/index.html", "r") as f:
    index = f.read()

label_value = classifier(user_input)[0]['label']

# 3) FOOTER
html_template = f'<style>{css}</style>\n{index.format(label=label_value)}'
html(html_template, width=800, height=300)
