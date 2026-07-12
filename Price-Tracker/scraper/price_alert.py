import pandas as pd

# Read latest merged data
df = pd.read_csv("merged_prices.csv")

# -----------------------------
# Set Target Prices
# -----------------------------

target_prices = {
    "P001": 170000,   # iPhone
    "P002": 70000,    # Samsung
    "P003": 60000,    # OnePlus
    "P004": 45000,    # Pixel
    "P005": 100000,   # HP Victus
    "P006": 90000,    # Lenovo
    "P007": 1200,     # boAt
    "P008": 4000,     # Sony
    "P009": 1000,     # Logitech
    "P010": 25000     # Apple Watch
}

print("=" * 60)
print("PRICE DROP ALERTS")
print("=" * 60)

alert_found = False

for _, row in df.iterrows():

    product_id = row["Product_ID"]

    current_price = min(
        row["Amazon_Price"],
        row["Flipkart_Price"]
    )

    target_price = target_prices[product_id]

    if current_price <= target_price:

        alert_found = True

        print(f"""
Product : {row['Product_Name_Amazon']}

Current Price : ₹{current_price}

Target Price  : ₹{target_price}

Platform : {row['Cheapest_Platform']}

🔥 BUY NOW!
""")

if not alert_found:
    print("No Product Reached Target Price.")

print("=" * 60)