import requests
from send_email import send_email

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=2622da6c958543e6a052cd7ccffb06e1&" \
      "language=pt"
api_key = "2622da6c958543e6a052cd7ccffb06e1"
request = requests.get(url)

content = request.json()

body = ""

for article in content["articles"][:20]:
    if (article["title"] is not None) and (article["description"] is not None):
        body = "Subject: Today's news" \
               + "\n" + body + "Titulo: " \
               + article["title"] + "\n" \
               + article["description"]  \
               + "\n" + article["url"] + 2*"\n"
    else:
        continue


body = body.encode("utf-8")

send_email(body)
