from newsplease import NewsPlease # for scraping web content
import requests
import json

# endpoint

def fetch_news(user_search):
    API_KEY = "94f7dc6dfe8e4c8485e4a8220c4c57f7"
    URL = f'https://newsapi.org/v2/top-headlines?q={user_search}&apiKey={API_KEY}'
    r = requests.get(URL)
    data = r.json()
    return data

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# array w/ all urls to articles from search results
urls = []
def get_search_results(data):
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        urls.append(article[attribute])
    return urls

# get source name of article based on site url
def get_source_name(index):
    url= urls[index]
    source_name = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            for x in article["source"]:
                                if x == "name":
                                    source_name = article["source"][x]
    return source_name

# get source id of article based on site url
def get_source_id(index):
    url= urls[index]
    source_id = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            for x in article["source"]:
                                if x == "id":
                                    source_id = article["source"][x]
    return source_id

# get author based on site url
def get_author(index):
    url= urls[index]
    author = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            author = article["author"]
    return author

# get unformatted content of article (truncated to 200 chars) based on site url
def get_content(url: str) -> str:
    article = NewsPlease.from_url(url)
    content = article.maintext
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            return content
    return "No content was found."

# get date based on site url
def get_date(index):
    url= urls[index]
    date = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            date = article["publishedAt"]
    return date


# get title of article based on site url
def get_title(index):
    url= urls[index]
    title = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            date = article["title"]
    return title

# get description of article based on site url
def get_description(index):
    url= urls[index]
    description = ""
    for item in data:
        if item == "articles":
            articles = data.get("articles")
            for article in articles:
                for attribute in article:
                    if attribute == "url":
                        if article[attribute] == url:
                            description = article["description"]
    return description