from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/get_news', methods=['GET'])
def get_news():
    url = "https://internationaldefenceanalysis.com/category/defense-news/"
    response = requests.get(url)
    articles_list = []

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        articles = soup.find_all('article')
        
        for article in articles:
            headline = article.find('h2', class_='entry-title').text.strip()
            image_url = article.find('img')['src']
            article_link = article.find('a')['href']
            
            articles_list.append({
                "headline": headline,
                "image_url": image_url,
                "article_link": article_link
            })
            
        return jsonify(articles_list)
    else:
        return jsonify({"error": "Failed to fetch articles"})

if __name__ == '__main__':
    app.run(debug=True)
