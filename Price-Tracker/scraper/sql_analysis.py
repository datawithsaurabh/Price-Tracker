import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("price_tracker.db")

# 1. View All Products
print("=" * 70)
print("ALL PRODUCTS")
query = "SELECT * FROM product_prices"
df = pd.read_sql(query, conn)
print(df)

# 2. Amazon Cheaper Products
print("=" * 70)
print("AMAZON CHEAPER PRODUCTS")
query = """
SELECT Product_Name_Amazon,
       Amazon_Price,
       Flipkart_Price
FROM product_prices
WHERE Amazon_Price < Flipkart_Price;
"""
print(pd.read_sql(query, conn))

# 3. Flipkart Cheaper Products
print("=" * 70)
print("FLIPKART CHEAPER PRODUCTS")
query = """
SELECT Product_Name_Amazon,
       Amazon_Price,
       Flipkart_Price
FROM product_prices
WHERE Flipkart_Price < Amazon_Price;
"""
print(pd.read_sql(query, conn))

# 4. Average Amazon Price
print("=" * 70)
print("AVERAGE AMAZON PRICE")
query = """
SELECT ROUND(AVG(Amazon_Price),2) AS Avg_Amazon_Price
FROM product_prices;
"""
print(pd.read_sql(query, conn))

# 5. Average Flipkart Price
print("=" * 70)
print("AVERAGE FLIPKART PRICE")
query = """
SELECT ROUND(AVG(Flipkart_Price),2) AS Avg_Flipkart_Price
FROM product_prices;
"""
print(pd.read_sql(query, conn))

# 6. Most Expensive Product
print("=" * 70)
print("MOST EXPENSIVE PRODUCT")
query = """
SELECT Product_Name_Amazon,
       Amazon_Price
FROM product_prices
ORDER BY Amazon_Price DESC
LIMIT 1;
"""
print(pd.read_sql(query, conn))

# 7. Brand Wise Average Price
print("=" * 70)
print("BRAND WISE AVERAGE AMAZON PRICE")
query = """
SELECT Brand_Amazon,
       ROUND(AVG(Amazon_Price),2) AS Average_Price
FROM product_prices
GROUP BY Brand_Amazon
ORDER BY Average_Price DESC;
"""
print(pd.read_sql(query, conn))

conn.close()

print("\nSQL Analysis Completed Successfully!")