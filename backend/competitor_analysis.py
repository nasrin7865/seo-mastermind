import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

def scrape_google_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")
    results = [h3.text for h3 in soup.find_all('h3')]
    
    return results[:5]  # Return top 5 results

@app.route('/competitor', methods=['POST'])
def competitor_analysis():
    data = request.json
    query = data['query']
    
    competitors = scrape_google_search(query)
    return jsonify({'competitors': competitors})

if __name__ == '__main__':
    app.run(port=5004)
