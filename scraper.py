from bs4 import BeautifulSoup
import requests


url = "https://paykoko.com/"
response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
print(soup)
items = soup.find_all(class_="post-item col-lg-3 col-md-4 col-sm-6")
for item in items:
    print(item)
