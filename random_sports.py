import requests
import random

def fetch_sports_articles():
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": "Category:Sports",
        "cmlimit": "500",
        "cmnamespace": "0",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = [item for item in data.get("query", {}).get("categorymembers", []) if item["ns"] == 0]
    return articles

def get_random_sports_article():
    articles = fetch_sports_articles()
    if not articles:
        print("No articles found in the Sports category.")
        return

    random_article = random.choice(articles)
    title = random_article["title"]
    page_id = random_article["pageid"]

    print(f"Title: {title}")
    print(f"Link: https://en.wikipedia.org/wiki?curid={page_id}")

get_random_sports_article()
