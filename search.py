from news_api import fetch_news, get_search_results

user_search = input("Enter a search: ")
data = fetch_news(user_search)
urls = get_search_results(data)
urls = [article['url'] for article in data['articles'][:3]]
#print(data)
#print(urls)