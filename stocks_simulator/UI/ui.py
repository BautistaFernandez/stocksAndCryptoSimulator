import tkinter as tk
from graphics.plotter import graphic_config, area_chart
import threading
import time

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stocks and Crypto")

        # Symbols.
        self.symbols = ["AAPL", "TSLA", "GOOG", "NVDA", "BTC-USD", "ETH-USD"]

        # Display area.
        self.canvas = area_chart(self.root)

        # Dopdown menu.
        self.selected_symbol = tk.StringVar(value=self.symbols[0])
        dropdown = tk.OptionMenu(self.root, self.selected_symbol, *self.symbols, command=self.display_chart)
        dropdown.pack()

    # Displays the chart for the selected symbol.
    def display_chart(self, symbol):
        graphic_config(self.canvas, symbol)

    # Automatically updates the chart.
    def update_chart(self, interval=180):
        def update():
            while True:
                symbol = self.selected_symbol.get()
                graphic_config(self.canvas, symbol)
                time.sleep(interval)

        # Start the thread for updating the chart periodically
        thread = threading.Thread(target=update, daemon=True)
        thread.start()

# Run the GUI
root = tk.Tk()
app = StockApp(root)

# Run the auto_update thread.
app.update_chart(interval=180)

root.mainloop()