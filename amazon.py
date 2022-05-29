# 19BCE0629-Samvit Swaminathan

#import libraries
from bs4 import BeautifulSoup
import requests
import urllib.request
from PIL import Image


# url from amazon of any random product
URL = 'https://www.amazon.in/ComicSense-xyz-Jujutsu-Kaisen-Itadori-Uniform/dp/B09J2BWT6R/ref=sr_1_1_sspa?keywords=anime+hoodie&qid=1646018519&sprefix=anime%2Caps%2C328&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFQOFFCVlFNR1lZNUQmZW5jcnlwdGVkSWQ9QTA2NzExMDUzSFJIS0czSTNPRFAxJmVuY3J5cHRlZEFkSWQ9QTA1MDc3MDgyWjU0OFlUTURSWjRYJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(URL, headers=headers)
s1 = BeautifulSoup(page.content, "html.parser")
s = BeautifulSoup(s1.prettify(), "html.parser")
# title
title = s.find(id='productTitle').get_text().strip()
# discount
discount = s.select_one('.a-color-price').get_text().strip()
# price
price = s.select_one('.a-offscreen').get_text().strip()
# image url
img_url = s.find(id='landingImage')['src'].strip()
print("Title of Product: ", title)
print("Price of Product: ", price)
print("Discount in Product: ", discount)
# display of image
urllib.request.urlretrieve(img_url, "Product Image")
img = Image.open("Product Image")
img.show()
