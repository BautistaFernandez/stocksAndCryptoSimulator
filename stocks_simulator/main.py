import time
from data.data_process import update_price, create_db, store_historical
from UI.ui import StockApp
import tkinter as tk
import threading
import sqlite3

# Symbols for app.
track_symbols = ['AAPL', 'TSLA', 'GOOG', 'NVDA', 'BTC-USD', 'ETH-USD']  # Symbols to track.

def checking_db():
    try:
        # Connect to the database (assumes it's in the current directory)
        connection = sqlite3.connect('stocks.db')
        cursor = connection.cursor()

        # Check if the 'prices' table has data
        cursor.execute('SELECT COUNT(*) FROM prices;')
        row_count = cursor.fetchone()[0]

        connection.close()

        if row_count > 0:
            return True
        else:
            return False

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

# Current archive "main".
if __name__ == "__main__":
    # Create db and load historical data
    create_db()

    checking = checking_db()

    if not checking:
        for symbol in track_symbols:
            store_historical(symbol)  # Inserts historical data in db.
    else:
        pass

    # Initialize the GUI
    root = tk.Tk()
    app = StockApp(root)

    # Update prices periodically in background thread
    def update_prices_continuously():
        while True:
            for symbol in track_symbols:
                update_price(symbol)
            time.sleep(180)  # Wait 3 minutes before next update

    # Start the price update thread
    price_update_thread = threading.Thread(target=update_prices_continuously, daemon=True)
    price_update_thread.start()

    root.mainloop()  # Run main loop from UI.
