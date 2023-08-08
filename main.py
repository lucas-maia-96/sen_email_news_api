import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-08&sortBy=publishedAt&apiKey=2622da6c958543e6a052cd7ccffb06e1"
api_key = "2622da6c958543e6a052cd7ccffb06e1"
request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
