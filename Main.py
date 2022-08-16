import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.uk/New-Apple-iPhone-12-128GB/dp/B08L5QVFCT"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

login = input("Enter your email")
passw = input("Enter your password/2FA code")

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-offscreen").get_text()
    converted_price = float(price[1:])

    if (converted_price < 500):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(login, passw)

    subject = "Price went down!"
    body = "Check the link at " + URL
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        login,
        login,
        msg
    )
    print("Email has been sent")

    server.quit()

while True:
    check_price()
    time.sleep(60*60*24)