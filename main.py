import requests
from send_email import send_email

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-07-08&sortBy=publishedAt&apiKey=2622da6c958543e6a052cd7ccffb06e1"
api_key = "2622da6c958543e6a052cd7ccffb06e1"
request = requests.get(url)

content = request.json()

body = ""

for article in content["articles"]:
    if (article["title"] is not None) and (article["description"] is not None):
        body = body + "Titulo: " + \
            article["title"] + "\n" + \
            article["description"] + "\n" + 18*"-" + 2*"\n"
    else:
        continue


body = body.encode("utf-8")

send_email(body)
