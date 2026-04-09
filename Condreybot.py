import requests
import time
from datetime import datetime

# Your secrets will be loaded from GitHub Secrets
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
TWELVE_DATA_KEY = os.environ.get('TWELVE_DATA_KEY')

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}, timeout=30)
        print("✅ Sent")
    except:
        pass

def get_price():
    try:
        url = f"https://api.twelvedata.com/price?symbol=EUR/USD&apikey={TWELVE_DATA_KEY}"
        r = requests.get(url, timeout=10)
        data = r.json()
        return float(data["price"]) if "price" in data else None
    except:
        return None

def run_bot():
    print("🤖 CondreyBot running...")
    price = get_price()
    
    if price:
        message = f"""
🤖 *CONDREYBOT - AUTO TRADING*

📊 EUR/USD: `{price:.5f}`
🕐 Time: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`

✅ Bot running on GitHub Actions!
📈 Monitoring market...
"""
        send_telegram(message)
        print(f"Sent: {price}")
    else:
        print("Failed to get price")

if __name__ == "__main__":
    run_bot()
