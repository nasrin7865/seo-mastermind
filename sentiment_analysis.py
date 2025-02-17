import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify

app = Flask(__name__)
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    data = request.json
    text = data['text']
    
    sentiment_score = sia.polarity_scores(text)
    
    return jsonify({'sentiment_score': sentiment_score})

if __name__ == '__main__':
    app.run(port=5003)
