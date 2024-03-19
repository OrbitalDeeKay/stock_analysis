import yfinance as yf
from colorama import Fore


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    average_price = round(data['Close'].mean(), 2)  # Price will be rounded up the second decimal
    print(Fore.BLUE + 'Средняя цена за период:', average_price)
    print(Fore.RESET)
