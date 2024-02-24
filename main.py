import requests
import lxml
from bs4 import BeautifulSoup

url = "https://kups.club/"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
session = requests.session()

for j in range(1, 11):
    print(f"PAGE = {j}")
    with open("nameandprice.txt", "a", encoding="UTF-8") as file:
        file.write(f"{j}\n")
        url = f"https://kups.club/page={j}/"
        response = session.get(url, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            allProduct = soup.find("div", class_="row mt-4")
            products = allProduct.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")

            for i in range(len(products)):
                try:
                    title = products[i].find("h3", class_="card-title").text.strip()
                    price = products[i].find("p", class_="card-text").text.strip()

                    with open("nameandprice.txt", "a", encoding="UTF-8") as file:
                        file.write(f"{title} --->>> {price}\n")
                except:
                    print("products not found")