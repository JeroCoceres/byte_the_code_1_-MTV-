from django.shortcuts import render, HttpResponse
import requests
from django_base.settings import NEWS_API_KEY
from news.models import News

def fetch_news(request):
    response = requests.get(f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={NEWS_API_KEY}").json()
    if response.status_code != 200:
        return HttpResponse(response.status_code)
    response = response.json()
    news_to_create = []
    for article in response ["articles"]:
        if all([article["title"],
                    article["description"],
                    article["url"],
                    article["urlToImage"],
                    article["publishedAt"]
                    ]):
            news_to_create.append(News(title = article["title"],description = article["description"], url_to_news = article["url"],
                url_to_image = article["urlToImage"], published_at = article["publishedAt"]))

    News.objects.bulk_create(news_to_create)
    return HttpResponse(response["articles"])


