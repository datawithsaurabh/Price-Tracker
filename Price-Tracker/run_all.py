import subprocess

steps = [
    ("Amazon Scraper", "scraper/amazon.py"),
    ("Flipkart Scraper", "scraper/flipkart.py"),
    ("Merge Prices", "scraper/merge_prices.py"),
    ("Update Database", "database.py"),
    ("Update History", "history.py"),
    ("Price Alerts", "price_alert.py"),
]

print("=" * 60)
print("PRICE TRACKER AUTOMATION STARTED")
print("=" * 60)

for step_name, script in steps:

    print(f"\nRunning: {step_name}")

    result = subprocess.run(["python", script])

    if result.returncode == 0:
        print(f"✅ {step_name} Completed")
    else:
        print(f"❌ {step_name} Failed")
        break

print("\n" + "=" * 60)
print("ALL TASKS FINISHED")
print("=" * 60)