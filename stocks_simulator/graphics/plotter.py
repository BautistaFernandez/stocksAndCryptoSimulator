import sqlite3
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Dark mode
plt.style.use('dark_background')

# Take historical data from db.
def take_historical(symbol):
    # Take historical data from db.
    connection = sqlite3.connect('stocks.db')
    cursor = connection.cursor()
    
    cursor.execute('''
                   SELECT date, price FROM prices WHERE symbol = ? ORDER BY date ASC
                   ''', (symbol,))
    rows = cursor.fetchall()
    connection.close()

    dates = [row[0] for row in rows]
    prices = [row[1] for row in rows]
    
    return dates, prices

# Graphic config.
def graphic_config(canvas, symbol):
    dates, prices = take_historical(symbol)

    #Clear previous chart and generates new one.
    fig = Figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    # Colors for dark mode.
    line_color = "#00BFFF"  # Graphic line.
    fill_color = "#00BFFF"  # Area's chart color.
    ax.plot(dates, prices, color=line_color, lw=2)
    ax.fill_between(dates, 0, prices, color=fill_color, alpha=0.3)

    # Backside and text.
    ax.set_facecolor("#1e1e1e")  # Backside.
    fig.patch.set_facecolor("#1e1e1e")  # Backside area around graphic.
    
    # Title and tags.
    ax.set_title(f"Price chart for {symbol}", color="white")
    ax.set_xlabel("Date", color="white")
    ax.set_ylabel("Price", color="white")
    ax.tick_params(colors="white")

    canvas.figure = fig
    canvas.draw_idle()

# Creates area chart.
def area_chart(master):
    fig = Figure(figsize=(8, 6))
    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.get_tk_widget().pack()

    return canvas