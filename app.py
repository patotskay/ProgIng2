import streamlit as st
from streamlit.components.v1 import html

from os import path as osp

from utils.settings import settings

if settings['MODEL'] == "our":
    from models.arifman import get_answer, get_toxic
else:
    from models.models import get_answer, get_toxic

from utils.language.ru import get_text_content

label_value = "N/A"

# получаем текстовый контент
main_title, sub_title = get_text_content()

# Сообщения для пользователя/бота
st.session_state['chat_history'] = []

# собираем страницу CSS из трех частей HTML:
# 0) добавляем общий файлк с CSS стилями
with open(osp.join(settings['SCRIPT_PATH'], "static", "css", "styles.css"), 'r') as f:
    css = f.read()

# 1) HEADER
# добавляем HTML-блок general-header
with open(osp.join(settings['SCRIPT_PATH'], "templates", "general", "header.html"), "r") as f:
    header = f.read()
html_template = f'<style>{css}</style>\n{header.format(title=main_title, sub_title=sub_title)}'
html(html_template, width=800, height=200)

# 2) MAIN
# создаем форму для ввода запросов
user_input = st.text_input("Вы: ")

# если пользователь ввел запрос, обрабатываем его
if user_input:
    # кодируем запрос пользователя и добавляем его в историю чата
    st.session_state['chat_history'].append(user_input)
    bot_response = get_answer(user_input)
    st.session_state['chat_history'].append(bot_response)
    for idx, ph in enumerate(st.session_state['chat_history']):
        if idx % 2 == 0:
            st.write("Вы: " + ph)
        else:
            if settings['MODEL'] == 'our':
                st.write("ArifMan: " + ph)
            else:
                st.write("Bot: " + ph)
    label_value = get_toxic(user_input)

# добавляем HTML-блок general-header
with open(osp.join(settings['SCRIPT_PATH'], "templates", "main", "index.html"), "r") as f:
    index = f.read()

# 3) FOOTER
html_template = f'<style>{css}</style>\n{index.format(label=label_value)}'
html(html_template, width=800, height=300)
