import sqlite3
from data.api import get_historical, get_data
import threading
import time

# Creates db and table.
def create_db():
    pass

# Stores historical data from api in db.
def store_historical(symbol):
    historical_data = get_historical(symbol)

    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()

    for date, row in historical_data.iterrows():
        price = row['Close']
        
        # Check if price is valid
        if price is None:
            print(f"Skipping entry for {symbol} on {date} due to missing price data.")
            continue  # Skip this iteration if price is None

        his_date = date.strftime("%Y-%m-%d")
        his_time = date.strftime("%H:%M:%S")
        
        try:
            cursor.execute('''
                INSERT INTO prices (symbol, date, time, price)
                VALUES (?, ?, ?, ?)
            ''', (symbol, his_date, his_time, price))
        except sqlite3.IntegrityError as e:
            print(f"Error inserting data for {symbol} on {date}: {e}")
            continue  # Skip entry if there's an error

    conn.commit()
    conn.close()

# Update last price in db.
def update_price(symbol, interval=180):
    def update():
        while True:
            price, date, times = get_data(symbol)

            conn = sqlite3.connect('stocks.db')
            cursor = conn.cursor()

            cursor.execute('''
                        INSERT INTO prices (symbol, date, time, price)
                        VALUES (?, ?, ?, ?)
                        ''', (symbol, date, times, price))
            
            conn.commit()
            conn.close()

            time.sleep(interval)
    
    # Updating for ever with thread.
    thread = threading.Thread(target=update, daemon=True)
    thread.start()
