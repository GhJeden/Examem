import requests
import lxml
from bs4 import BeautifulSoup

url = "https://kups.club/"

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
session = requests.session()

for j in range(1, 10):
    print(f"PAGE = {j}")
    with open("nameandprice.txt", "a", encoding="UTF-8") as file:
        file.write(f"{j}\n")
        url = f"https://kups.clubpage={j}/"
        response = session.get(url, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            allProduct = soup.find("div", class_="row col-lg-4 col-md-4 col-sm-6")
            products = allProduct.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")

            for i in range(len(products)):
                try:
                    title = products[i].find("div", class_="shop_title").text.strip()
                    price = products[i].find("div", class_="shop_rate").text.strip()

                    with open("nameandprice.txt", "a", encoding="UTF-8") as file:
                        file.write(f"{title} --->>> {cashback}\n")
                except:
                    print("products not found")