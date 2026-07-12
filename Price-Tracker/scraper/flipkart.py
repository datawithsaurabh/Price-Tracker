import pandas as pd
from playwright.sync_api import sync_playwright
from datetime import datetime

# Read Excel File
df = pd.read_excel("products.xlsx")


# Function to Scrape Flipkart Data
def get_flipkart_data(page):

    product_title = page.locator("h1").inner_text(timeout=10000).strip()

    price_locators = page.locator("div.v1zwn20")

    current_price = None

    for i in range(price_locators.count()):
        text = price_locators.nth(i).inner_text().strip()

        if "₹" in text and "%" not in text:
            current_price = text
            break

    if current_price is None:
        raise Exception("Price not found")

    clean_price = (
        current_price
        .replace("₹", "")
        .replace(",", "")
        .strip()
    )

    clean_price = int(clean_price)

    return product_title, clean_price


results = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    for index, row in df.iterrows(): 
        

        try:

            flipkart_url = row["Flipkart_URL"]

            page.goto(flipkart_url, timeout=60000)

            page.wait_for_timeout(10000)

            title, price = get_flipkart_data(page)

            print("-" * 60)
            print(title)
            print(price)

            results.append({
                "Product_ID": row["Product_ID"],
                "Product_Name": row["Product_Name"],
                "Brand": row["Brand"],
                "Category": row["Category"],
                "Flipkart_Product_Title": title,
                "Flipkart_Price": price,
                "Flipkart_URL": flipkart_url,
                "Status": "Success",
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
                "Flipkart_Product_Title": None,
                "Flipkart_Price": None,
                "Flipkart_URL": flipkart_url,
                "Status": "Failed",
                "Scrape_Date": datetime.now().strftime("%Y-%m-%d"),
                "Scrape_Time": datetime.now().strftime("%H:%M:%S")
            })

    results_df = pd.DataFrame(results)

    print(results_df)

    results_df.to_csv(
        "flipkart_prices.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print("Flipkart CSV Saved Successfully!")