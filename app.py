import flask
import io
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
from sklearn.metrics.pairwise import cosine_similarity

def nlp(text):
    text = text.strip().lower()
    t = ""
    for i in text:
        if i.isalpha() or i.isnumeric() or i==" ":
            t+=i
    text = t
    return text

def similarity(string_1, string_2):
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    from sklearn.metrics.pairwise import cosine_similarity

    string_1 = nlp(string_1)
    string_2 = nlp(string_2)

    string_1, string_2 = vectorizer.fit_transform([string_1, string_2])
    score = cosine_similarity(string_1, string_2)[0][0]
    print(score)
     
    #return jsonify({'val': score})
    return str(score)

app = Flask(__name__)

@app.route('/')
def welcome():
   return "Strings Similarity API"

@app.route('/predict', methods=['POST', 'GET']) 
def pridict():
    #if request.method == "GET":
    data = request.json
    string_1 = data['text1']
    string_2 = data['text2']
    return similarity(string_1, string_2)


if __name__ == '__main__':
    app.run(debug=True)