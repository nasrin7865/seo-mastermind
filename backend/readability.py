import textstat
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/readability', methods=['POST'])
def readability_analysis():
    data = request.json
    text = data['text']
    
    readability_score = textstat.flesch_reading_ease(text)
    
    return jsonify({'readability_score': readability_score})

if __name__ == '__main__':
    app.run(port=5001)
