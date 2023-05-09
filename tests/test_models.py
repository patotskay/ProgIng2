from models.models import *


user_input = 'Hello'
models = get_models()
response = get_answer(user_input)
sentiment = models[0](user_input)[0]['label']


def test_get_models():
    global models
    assert len(models) == 3


def test_get_answer():
    global response
    assert type(response) is str


def test_get_toxic():
    global sentiment
    assert sentiment == 'POSITIVE'