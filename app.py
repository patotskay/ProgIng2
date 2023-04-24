import streamlit as st
from streamlit.components.v1 import html

from models.models import get_models
from utils.language.ru import get_text_content
from utils.settings import settings

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
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(
        input_ids, max_length=settings['MAX_HISTORY_LEN'], pad_token_id=tokenizer.eos_token_id
    )

    # декодируем ответ бота и выводим его на страницу
    bot_response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    st.write("Bot: " + bot_response)

# добавляем HTML-блок general-header
with open("templates/main/index.html", "r") as f:
    index = f.read()

label_value = classifier(user_input)[0]['label']

# 3) FOOTER
html_template = f'<style>{css}</style>\n{index.format(label=label_value)}'
html(html_template, width=800, height=300)
