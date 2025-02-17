import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/trend', methods=['POST'])
def predict_seo_trend():
    data = request.json
    keyword_data = np.array(data['trend_data']).reshape(-1, 1)
    
    model = LinearRegression()
    model.fit(keyword_data, np.arange(len(keyword_data)))
    
    future_trend = model.predict([[len(keyword_data) + 1]])[0]
    
    return jsonify({'predicted_trend': future_trend})

if __name__ == '__main__':
    app.run(port=5005)
