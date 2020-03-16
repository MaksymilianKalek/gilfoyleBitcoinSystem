import requests
from bs4 import BeautifulSoup
import time
from playsound import playsound

URL = "https://cryptowat.ch/"

isLower = False

while True:
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="w-full self-center text-center pt-0 max-w-5xl py-10 mb-8 _1K8ogAIHDilfBifIr6WXip")
    if results is None:
        continue

    price = results.find_all("div", class_="text-right _2yv_NtK1R_FBVWqrvRdgcN _2jRRJJvarKXJGP9oRP-Bv0 _1TuQ_Cac70IaRi6hBmwL9")
    price = float(price[0].find("span", class_="price").text.strip())

    rate = 4630.0

    if price < rate:
        print(f"\n{price} is lower than {rate}$")
        if isLower == False:
            playsound("yousuffer.mp3")
            isLower = True
    else:
        print(f"\n{price} is higher than {rate}$")
        isLower = False

    time.sleep(3.0)