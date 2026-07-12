import pandas as pd

# Read CSV Files
amazon_df = pd.read_csv("amazon_prices.csv")
flipkart_df = pd.read_csv("flipkart_prices.csv")

# Merge Both DataFrames
merged_df = pd.merge(
    amazon_df,
    flipkart_df,
    on="Product_ID",
    suffixes=("_Amazon", "_Flipkart")
)

# Price Difference
merged_df["Price_Difference"] = (
    merged_df["Amazon_Price"] -
    merged_df["Flipkart_Price"]
)

# Cheapest Platform
merged_df["Cheapest_Platform"] = merged_df.apply(
    lambda row: "Amazon"
    if row["Amazon_Price"] < row["Flipkart_Price"]
    else "Flipkart",
    axis=1
)

print(merged_df)

merged_df.to_csv(
    "merged_prices.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Merged CSV Saved Successfully!")