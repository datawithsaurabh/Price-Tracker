# 🛒 Price Tracker Dashboard

An end-to-end **Price Tracking & Comparison System** built using **Python, Playwright, SQL, Excel, and Power BI**. The project automatically scrapes product prices from **Amazon** and **Flipkart**, stores the data, compares prices, tracks historical changes, and visualizes insights in an interactive Power BI dashboard.

---

## 📊 Dashboard Preview

> Add your dashboard screenshot here.

![Dashboard Preview](screenshots/dashboard.png)

---

## 🚀 Features

- 🔍 Scrapes live product prices from Amazon & Flipkart
- 📦 Supports multiple products from Excel input
- 📊 Interactive Power BI Dashboard
- 💰 Amazon vs Flipkart price comparison
- 📈 Price history tracking
- 🔔 Price difference analysis
- 📂 SQL database integration
- 🎯 Interactive filters by Brand, Category & Cheapest Platform
- 📉 Brand-wise average price analysis
- 🥧 Category distribution analysis
- 📋 Product comparison table with conditional formatting

---

## 🛠 Tech Stack

### Programming

- Python

### Data Processing

- Pandas
- OpenPyXL

### Web Scraping

- Playwright

### Database

- SQLite

### Data Visualization

- Microsoft Power BI

### Other Tools

- Microsoft Excel
- Git
- GitHub

---

# 📂 Project Structure

```text
Price-Tracker/
│
├── dashboard/
│   └── price_tracker_dashboard.pbix
│
├── data/
│   ├── products.xlsx
│   ├── amazon_prices.csv
│   ├── flipkart_prices.csv
│   ├── merged_prices.csv
│   ├── price_history.csv
│   └── price_tracker.db
│
├── scraper/
│   ├── amazon.py
│   ├── flipkart.py
│   ├── database.py
│   ├── history.py
│   ├── price_alert.py
│   └── sql_analysis.py
│
├── screenshots/
│   └── dashboard.png
│
├── logo/
├── run_all.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Workflow

```text
Products.xlsx
        │
        ▼
Python Scraper
(Amazon + Flipkart)
        │
        ▼
CSV Files
        │
        ▼
SQLite Database
        │
        ▼
Merged Dataset
        │
        ▼
Power BI Dashboard
```

---

# 📈 Dashboard KPIs

- Total Products
- Average Amazon Price
- Average Flipkart Price
- Highest Product Price
- Average Price Difference

---

# 📊 Dashboard Visuals

- Amazon vs Flipkart Price Comparison
- Cheapest Platform Analysis
- Brand-wise Average Price
- Category Distribution
- Product Comparison Table
- Interactive Filters
- Business Insights

---

# ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Price-Tracker.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Scraper

```bash
python run_all.py
```

### 4️⃣ Refresh Power BI Dashboard

Open:

```
dashboard/price_tracker_dashboard.pbix
```

Click:

```
Home → Refresh
```

---

# 📌 Future Improvements

- Email Price Alerts
- Telegram Notifications
- Daily Scheduled Scraping
- Streamlit Web Application
- MySQL Integration
- Cloud Deployment
- Historical Price Trend Dashboard

---

# 👨‍💻 Author

**Saurabh Shivkriti**

📧 saurabhshivkriti1001@gmail.com

💼 Aspiring Data Analyst

⭐ If you like this project, don't forget to give it a star.
