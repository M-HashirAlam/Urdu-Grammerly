import numpy as np
from flask import Flask, render_template, request, jsonify
import sqlite3
from oposite import *
# from correction import correct
from without import find_closest_words
from prediction import predict_next_word
from utils import parese_sentence

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check')
def search():
    return render_template('second1.html')


@app.route('/keyboard')
def keyboard():
    return render_template("keyboard.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/grammar')
def grammar():
    return render_template("grammar.html")
@app.route('/correct', methods=['POST'])
def process():
    input_text = request.json.get('input_text', '')
    word_list = open('wordlist.txt', "r+", encoding="utf-8").read().split()
    incorrect_words = {}
    input_sentence = input_text.rstrip('.')
    sentence_endings = ['۔', '.', '!', '?', " "]
    input_sentence = input_text.strip()
    for ending in sentence_endings:
        if input_sentence.endswith(ending):
            input_sentence = input_sentence[:-1]
    for word in input_sentence.split():
        if word not in word_list:
            suggestions = find_closest_words(word, word_list)
            if suggestions:
                incorrect_words[word] = suggestions
    return jsonify(incorrect_words)


# @app.route('/check', methods=['POST'])
# def check():
#     text = str(request.form["words"])
#     a = correct(text)
#     return jsonify({'text': a})

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['words']
    predicted_word = predict_next_word(input_text)
    response = jsonify({'text': predicted_word})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/guide', methods=['POST'])
def guide():
    if request.method == 'POST':
        input_sent = request.form['sentence']
        tags = parese_sentence(input_sent)
        return jsonify(tags)
@app.route('/get_ner', methods=['POST'])
def get_ner():
    user_input = request.form['user_input']
    # user_input = request.form['editor']

    ner_result = Ner(user_input)
    # ner_result = Ner(user_input)
    return jsonify({"result": ner_result})


@app.route('/get_synonyms', methods=['POST'])
def get_synonyms():
    user_input = request.form['user_input']
    synonyms_result = get_synonyms_from_database(user_input)
    return jsonify({"result": synonyms_result})


@app.route('/get_opposite', methods=['POST'])
def get_opposite():
    user_input = request.form['user_input']
    opposite_result = get_opposite_from_database(user_input)
    return jsonify({"result": opposite_result})


@app.route('/get_male_female', methods=['POST'])
def get_male_female():
    user_input = request.form['user_input']
    male_female_result = get_male_female_from_database(user_input)
    return jsonify({"result": male_female_result})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
