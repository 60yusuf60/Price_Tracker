# Price Tracker 🛒💰

A Python project to track product prices from a website and notify via email if the price drops below a threshold. This project is ideal for learning **web scraping**, **data analysis**, and **automation** with Python.

---

## Features ✨

- Fetch product page using `requests` and parse HTML with `BeautifulSoup`
- Extract product title and current price
- Save price history to a CSV file (`price_history.csv`)
- Visualize price trends using `matplotlib`
- Send email alert when the price drops below a user-defined threshold
- UTF-8 compatible for currency symbols (like £, $, €)

---

## How It Works 🔧

1. **Fetch the page**: Uses `requests` with headers to access the webpage  
2. **Parse HTML**: `BeautifulSoup` extracts the price and product title  
3. **Save data**: Prices are appended with timestamps in `price_history.csv`  
4. **Plot graph**: Historical prices are plotted for visual trend analysis  
5. **Send email alert**: If the price is below the threshold, an email is sent  

---

## Usage 🚀

1. Install required packages:

```bash
pip install -r requirements.txt