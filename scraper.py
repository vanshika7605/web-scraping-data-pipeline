import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 51):

    url = f"http://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

df = pd.DataFrame(data)

# Clean price column
df["Price"] = df["Price"].str.replace("Â£","", regex=False)
df["Price"] = df["Price"].astype(float)

# Save cleaned data
df.to_csv("books_data.csv", index=False)

print("Scraping completed!")