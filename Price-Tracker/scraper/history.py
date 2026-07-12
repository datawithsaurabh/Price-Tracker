import pandas as pd
import os

# Read latest merged data
latest_df = pd.read_csv("merged_prices.csv")

history_file = "price_history.csv"

# Check if history file already exists
if os.path.exists(history_file):

    history_df = pd.read_csv(history_file)

    # Append new data
    history_df = pd.concat([history_df, latest_df], ignore_index=True)
    history_df = history_df.drop_duplicates(
            subset=[
                "Product_ID",
                "Amazon_Price",
                "Flipkart_Price"
            ],
            keep="last"
        )

else:

    # First time create history file
    history_df = latest_df
    

# Save updated history
history_df.to_csv(
    history_file,
    index=False,
    encoding="utf-8-sig"
)

print("Price History Updated Successfully!")
print(history_df.tail())