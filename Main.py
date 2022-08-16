import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5QVFCT"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-offscreen").get_text()
    converted_price = float(price[1:])

    print(title.strip())
    print(converted_price)