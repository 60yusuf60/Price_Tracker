# -------------------------
# IMPORTS AND LIBRARIES
# -------------------------
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
import smtplib

# -------------------------
# TARGET URL AND HEADERS
# -------------------------
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

headers = {
    "User-Agent" : "Mozilla/5.0"
}

# -------------------------
# FETCHING THE PAGE
# -------------------------
response = requests.get(url, headers=headers)

response.encoding = "utf-8"

if response.status_code == 200:
    print("Page successfully fetched!")
else:
    print("Failed to fetch page. Status code:", response.status_code)

# -------------------------
# PARSING HTML WITH BEAUTIFULSOUP
# -------------------------
soup = BeautifulSoup(response.text, "html.parser")

print("Page title: ",soup.title.text.strip())

price_element  = soup.find("p", class_="price_color")

price = price_element.text

print("Current price: ",price)

price_text = price_element.text
price_value = float(price_text.replace("£",""))

# -------------------------
# CSV FILE SETUP
# -------------------------
csv_file = "price_history.csv"

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date","price"])

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([datetime.now(), price_value])

print(f"Price saved to {csv_file}")

# -------------------------
# DATA ANALYSIS AND PLOTTING
# -------------------------
data=pd.read_csv("price_history.csv")

data["date"] =pd.to_datetime(data["date"])

plt.figure(figsize = (10,5))
plt.plot(data['date'], data['price'], marker='o', linestyle='-')
plt.title("Price History")
plt.xlabel("Date")
plt.ylabel("Price (£)")
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -------------------------
# PRICE ALERT SETTINGS
# -------------------------
threshold_price = 52

if price_value < threshold_price:

    sender_email = "yourmail@gmail.com"
    receiver_email = "yourmail@gmail.com"
    password = "your_app_password"

    subject= "Price Drop Alert!"
    body = f"The price dropped to £{price_value}!\nCheck the product: {url}"

    # -------------------------
    # SENDING EMAIL ALERT
    # -------------------------
    message=f"Subject: {subject}\n\n{body}".encode("utf-8")

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

    print("Price drop email sent!")