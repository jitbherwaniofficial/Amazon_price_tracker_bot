import requests as req
import lxml
from bs4 import BeautifulSoup
import smtplib

# SCRAPING #

url = "https://www.amazon.in/dp/B09SZTXHC4"
header =  {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept-Language":"en-US,en;q=0.5"
}

res = req.get(url,headers=header)

soup =  BeautifulSoup(res.content,"lxml")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.replace("₹","")
price_as_float = float(price_without_currency.replace(",",""))
print(price_as_float)


# SMTP #

title = soup.find(id="productTitle").get_text().strip()
# print(title)

buy_price = 110000
my_email = "programmerjit@gmail.com"
password = "rfxydcqqcvjpcmku"

if price_as_float < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com" , port=587) as connection:
        connection.starttls()
        result = connection.login(my_email,password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jitbherwani92@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )