import pandas as pd
from playwright.sync_api import sync_playwright
from datetime import datetime

df = pd.read_excel("products.xlsx")

def get_amazon_data(page):

    product_title = page.locator("span#productTitle").inner_text().strip()

    current_price = page.locator(".a-price-whole").first.inner_text()

    clean_price = current_price.replace(",", "").replace(".", "")

    clean_price = int(clean_price)

    return product_title, clean_price

results = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    for index, row in df.iterrows():

        try:

            amazon_url = row["Amazon_URL"]

            page.goto(amazon_url, timeout=60000)

            page.wait_for_timeout(5000)

            title, price = get_amazon_data(page)

            print("-" * 60)
            print(title)
            print(price)

            results.append({
                "Product_ID": row["Product_ID"],
                "Product_Name": row["Product_Name"],
                "Brand": row["Brand"],
                "Category": row["Category"],
                "Amazon_Product_Title": title,
                "Amazon_Price": price,
                "Status": "Success",
                "Amazon_URL": amazon_url,
                "Scrape_Date": datetime.now().strftime("%Y-%m-%d"),
                "Scrape_Time": datetime.now().strftime("%H:%M:%S")
            })

        except Exception as e:

            print("-" * 60)
            print("ERROR")
            print(row["Product_Name"])
            print(e)

            results.append({
                "Product_ID": row["Product_ID"],
                "Product_Name": row["Product_Name"],
                "Brand": row["Brand"],
                "Category": row["Category"],
                "Amazon_Product_Title": None,
                "Amazon_Price": None,
                "Amazon_URL": amazon_url,
                "Status": "Failed",
                "Scrape_Date": datetime.now().strftime("%Y-%m-%d"),
                "Scrape_Time": datetime.now().strftime("%H:%M:%S")
            })
results_df = pd.DataFrame(results)

print(results_df)      

results_df.to_csv(
    "amazon_prices.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV Saved Successfully!")