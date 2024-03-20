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
    print(Fore.BLUE + 'Средняя цена за период:', average_price, Fore.RESET)
    # print(Fore.RESET)


def notify_if_strong_fluctuations(data, threshold=10):
    max_price = data['Close'].max()
    min_price = data['Close'].min()
    price_diff = max_price - min_price
    price_change_percent = round((price_diff / min_price) * 100, 2)

    if price_change_percent > threshold:
        print(Fore.RED + f"Предупреждение: Сильные колебания в цене акций ({price_change_percent}% разницы)",
              Fore.RESET)
