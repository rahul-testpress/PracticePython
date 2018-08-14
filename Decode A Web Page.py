import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
title_list = []

soup = BeautifulSoup(requests.get(url).text, "html.parser")
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
    title_list.append(row.text)
for i in range(0, len(title_list)):
    print(title_list[i])
