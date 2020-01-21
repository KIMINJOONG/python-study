import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get("https://www.naver.com")
# response.html.links

response = requests.get("https://www.naver.com")
# print(response.headers)
# print(response.status_code)
bs = BeautifulSoup(response.text, "html.parser")

for img in bs.select("img"):
    print(img)

for a in bs.select("a"):
    print(a)