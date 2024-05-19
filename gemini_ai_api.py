from flask import Flask, request, Response, send_file
import os
import sys
import requests
import google.generativeai as genai
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from bias_factors.political_view.with_csv import calculate_bias_level
from news_api import get_date
from datetime import datetime

app = Flask(__name__)

genai.configure(api_key="AIzaSyDpB_WmhmXeeDoRy5pNNQtQ_V0nOHkgvHc")
model = genai.GenerativeModel('gemini-pro')

def get_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def generate_story(url):
    if url:
        article_content = get_article_content(url)
        if article_content:
            prompt = "Determine if this article is left or right wing and display the key words that indicate to one end" + article_content[:1000]
            bias_ratio, leaning = calculate_bias_level(url)
            bias_percent = round(bias_ratio*100, 2)
            response = model.generate_content(prompt)
            iframe_html = f'<iframe src="/bias_scale" width="30%" height="50px" style="border: none;"></iframe>'

            return f"{response.text}"
        else:
            return "Unable to fetch content from the provided URL."
    else:
        return "Please provide a valid URL."


@app.route('/bias_scale', methods=['GET'])
def bias_scale():
    
    return send_file('bias_scale.html')


if __name__ == '__main__':
    app.run(debug=False)