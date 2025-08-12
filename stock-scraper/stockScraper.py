#!/usr/bin/env python3
"""
Stock Price Scraper using yfinance API
A reliable way to get real stock data
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import time


class StockDataFetcher:
    def __init__(self):
        self.session = None

    def get_stock_data(self, symbol):
        """Get comprehensive stock data using yfinance"""
        try:
            # Create ticker object
            ticker = yf.Ticker(symbol)

            # Get current info
            info = ticker.info

            # Get recent price data (last 5 days)
            hist = ticker.history(period="5d")

            if hist.empty:
                return None

            # Get the most recent data
            latest = hist.iloc[-1]

            return {
                'symbol': symbol.upper(),
                'current_price': round(latest['Close'], 2),
                'open': round(latest['Open'], 2),
                'high': round(latest['High'], 2),
                'low': round(latest['Low'], 2),
                'volume': int(latest['Volume']),
                'market_cap': info.get('marketCap', 'N/A'),
                'pe_ratio': info.get('trailingPE', 'N/A'),
                'company_name': info.get('longName', symbol),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            return {
                'symbol': symbol.upper(),
                'current_price': None,
                'error': str(e),
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }

    def fetch_multiple_stocks(self, symbols):
        """Fetch data for multiple stocks"""
        results = []

        print(f"Fetching data for {len(symbols)} stocks...")

        for i, symbol in enumerate(symbols, 1):
            print(f"({i}/{len(symbols)}) Fetching {symbol}...", end=" ")

            data = self.get_stock_data(symbol)
            results.append(data)

            if data and data.get('current_price'):
                print(f"${data['current_price']}")
            else:
                print("Failed")

            # Small delay to be respectful
            time.sleep(0.1)

        return results

    def save_to_csv(self, data, filename='stock_data.csv'):
        """Save data to CSV"""
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"\nData saved to {filename}")
        return df

    def get_market_data_summary(self, symbols):
        """Get a nice summary of market data"""
        data = self.fetch_multiple_stocks(symbols)

        # Filter successful results
        successful_data = [d for d in data if d.get('current_price') is not None]

        if not successful_data:
            print("No data retrieved successfully")
            return None

        df = pd.DataFrame(successful_data)

        print("\n" + "=" * 80)
        print("MARKET DATA SUMMARY")
        print("=" * 80)

        for _, row in df.iterrows():
            print(f"{row['symbol']:6} | {row['company_name'][:40]:40} | ${row['current_price']:8.2f}")

        print("=" * 80)

        return df


def main():
    """Main function"""
    # Popular stocks to track
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA', 'AMZN', 'META', 'NFLX']

    # Create fetcher
    fetcher = StockDataFetcher()

    # Get data and display summary
    df = fetcher.get_market_data_summary(stocks)

    # Save to CSV
    if df is not None:
        fetcher.save_to_csv(df.to_dict('records'))

        # Show some basic analysis
        print(f"\nQuick Analysis:")
        print(f"Highest price: {df.loc[df['current_price'].idxmax(), 'symbol']} (${df['current_price'].max():.2f})")
        print(f"Lowest price: {df.loc[df['current_price'].idxmin(), 'symbol']} (${df['current_price'].min():.2f})")
        print(f"Average price: ${df['current_price'].mean():.2f}")


# Alternative: Simple price checker function
def quick_price_check(symbols):
    """Quick function to just get current prices"""
    print("Quick Price Check:")
    print("-" * 30)

    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            if not hist.empty:
                price = hist['Close'].iloc[-1]
                print(f"{symbol:6}: ${price:.2f}")
            else:
                print(f"{symbol:6}: No data")
        except:
            print(f"{symbol:6}: Error")


if __name__ == "__main__":
    print("Stock Data Fetcher")
    print("Choose an option:")
    print("1. Full data fetch (detailed)")
    print("2. Quick price check")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "2":
        symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA']
        quick_price_check(symbols)
    else:
        main()