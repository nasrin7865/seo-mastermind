import spacy
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return list(set(keywords))

@app.route('/keywords', methods=['POST'])
def keywords():
    data = request.json
    text = data['text']
    
    keywords = extract_keywords(text)
    return jsonify({'keywords': keywords})

if __name__ == '__main__':
    app.run(port=5002)
