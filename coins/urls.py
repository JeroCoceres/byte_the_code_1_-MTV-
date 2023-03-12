from django.urls import path
from coins.views import coins


urlpatterns = [
    path("coins", coins, name="fetch_news"),
]