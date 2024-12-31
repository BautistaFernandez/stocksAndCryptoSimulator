STOCKS SIMULATOR
#### Description: 

    This project that I did is a Windows application developed completely in Python. It is a stock and cryptocurrency simulator that allows you to view historical and current price charts. The application has a friendly user interface, where the user can select between different financial assets, such as stocks and cryptocurrencies, to observe the evolution of their prices over time.  

    The graph displayed on the interface is generated using historical data from up to 5 years ago, allowing the user to analyze past trends. The app connects to a database to store both historical prices and current prices, which are automatically updated every 3 minutes. With a button on the interface, the user can choose the desired asset and view its evolution graph.  

    This project took me about 2 or 3 months to complete. During this time, I faced numerous technical challenges, especially in integrating libraries and creating a seamless user experience. However, the result is a functional and modular application, designed to be scalable and efficient.

    ## Data Structure:
    stock_simulator/
    ├── main.py
    ├── README.md
    ├── requeriments.txt
    ├── stocks.db
    ├── data/
    │   ├── data_process.py
    │   └── api.py
    ├── UI/
    │   └── ui.py
    ├── graphics/
    │   └── plotter.py

    # Detail of Purpose and Functionalities per File  

    ## **data/api.py**  
    This file contains the main functions for interacting with the Yahoo Finance API, using the `yfinance` library.

    - **Obtaining current prices:**  
        The first function connects to this API and gets the current price of a stock or cryptocurrency.  
    - **Obtaining historical data:**  
        The second function gets historical data for the last 5 years and returns it in a format ready to store or use directly in charts.

    ## **data/data_process.py**  
    This file manages data processing and storage:  

    - **Create the database:**  
        Defines and generates the SQLite database with the necessary structure.  
    - **Store historical data:**  
        Inserts the data obtained from `api.py` into the database.  
    - **Update current prices:**  
        It uses a thread to automatically update the prices of selected stocks or cryptocurrencies every 3 minutes, keeping the information up to date.

    ## **graphics/plotter.py**  
    This file defines the logic to create the graphs displayed in the interface:  

    - **Obtaining historical data:**  
        It connects to the database to obtain the stored prices.  
    - **Chart Settings:**  
        Use `matplotlib` to create plots with an attractive visual design, including clear labels and titles.  
    - **Creation of area charts:**  
        Generate a graph that highlights price evolution with an aesthetic design.

    ## **UI/ui.py**  
    This file configures the graphical user interface, created with `tkinter`:  

    - **Asset selection:**  
        It includes a drop-down menu for the user to choose from available assets, such as AAPL, TSLA, BTC-USD, among others. Selecting one updates the displayed graph.  
    - **Automatic chart update:**  
        It uses a thread to update the graph periodically, ensuring always up-to-date data without needing to restart the application.  

    ## **main.py**  
    The main project file orchestrates the execution of all components:  

    - **Database initialization:**  
        Ensures that the database is configured and contains historical data for the selected assets.  
    - **UI execution:**  
        Call `ui.py` to launch the main window, allowing the user to interact with the graphs and data.

    ## **requirements.txt**  
    This file was automatically generated with `pip freeze` and contains all the libraries needed to run the application, such as `yfinance`, `matplotlib`, and `tkinter`. This makes it easy to quickly install dependencies.  

    ## **stocks.db**  
    This SQLite database stores the historical and current price information of selected stocks and cryptocurrencies. This allows quick access to data and ensures that the application works even without an internet connection.