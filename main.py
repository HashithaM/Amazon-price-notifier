import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# http://myhttpheader.com/

URL = "https://www.amazon.com/Kingston-500G-2280-Internal-SNV2S/dp/B0BBWJH1P8/ref=sr_1_1_sspa?crid=19ZWUS9R5UZJL&keywords=ssd%2B500gb%2Bkingston&qid=1689969714&sprefix=ssd%2B500gb%2Bkin%2Caps%2C358&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen")
price_without_currency = price.getText().split("$")[1]
price_as_float = float(price_without_currency)


def send_mail():
    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="kanthiwijesinghe71@gmail.com",
                            msg="subject:SSD Price Drop\n\n"
                                "Kingston 512 SSD in now lower than $25.\n"
                                "https://www.amazon.com/Kingston-500G-2280-Internal-SNV2S/dp/B0BBWJH1P8/ref=sr_1_1_sspa?crid=19ZWUS9R5UZJL&keywords=ssd%2B500gb%2Bkingston&qid=1689969714&sprefix=ssd%2B500gb%2Bkin%2Caps%2C358&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
        connection.close()


if price_as_float < 30:
    send_mail()
