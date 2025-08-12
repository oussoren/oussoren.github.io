#!/usr/bin/env python3


import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import time
import matplotlib.pyplot as plt


class AdvancedStockAnalyzer:
    def __init__(self):
        self.data_cache = {}

    # scrape all the information for the stock given a symbol and period
    def get_comprehensive_data(self, symbol, period="1y"):

        #use try except to avoid errors with inputting symbols incorrectly or with missing data
        try:
            #use yfinance to extract all the information
            ticker = yf.Ticker(symbol)
            info = ticker.info

            # get historical data
            hist = ticker.history(period=period)

            # get financial statements
            financials = ticker.financials
            balance_sheet = ticker.balance_sheet
            cashflow = ticker.cashflow

            # get dividends, splits, and recommendations if available
            dividends = ticker.dividends
            splits = ticker.splits
            recommendations = ticker.recommendations

            return {
                'basic_info': self._extract_basic_info(info),
                'price_data': self._extract_price_data(hist),
                'financial_metrics': self._extract_financial_metrics(info),
                'technical_indicators': self._calculate_technical_indicators(hist),
                'dividends': dividends.to_dict() if not dividends.empty else {},
                'stock_splits': splits.to_dict() if not splits.empty else {},
                'analyst_recommendations': recommendations.tail(5).to_dict(
                    'records') if recommendations is not None else [],
                'financial_statements': {
                    'income_statement': financials.to_dict() if financials is not None else {},
                    'balance_sheet': balance_sheet.to_dict() if balance_sheet is not None else {},
                    'cash_flow': cashflow.to_dict() if cashflow is not None else {}
                }
            }

        except Exception as e:
            print(f"Error fetching comprehensive data for {symbol}: {e}")
            return None

    #extract company information for self assessment(quality)
    def _extract_basic_info(self, info):
        return {
            'company_name': info.get('longName', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'country': info.get('country', 'N/A'),
            'website': info.get('website', 'N/A'),
            'business_summary': info.get('longBusinessSummary', 'N/A'),
            'employees': info.get('fullTimeEmployees', 'N/A'),
            'market_cap': info.get('marketCap', 'N/A'),
            'enterprise_value': info.get('enterpriseValue', 'N/A')
        }

    #extracts recent price data for other financial metric calculation
    def _extract_price_data(self, hist):
        if hist.empty:
            return {}

        latest = hist.iloc[-1]
        week_ago = hist.iloc[-5] if len(hist) >= 5 else hist.iloc[0]
        month_ago = hist.iloc[-20] if len(hist) >= 20 else hist.iloc[0]

        return {
            'current_price': round(latest['Close'], 2),
            'open': round(latest['Open'], 2),
            'high_52_week': round(hist['High'].max(), 2),
            'low_52_week': round(hist['Low'].min(), 2),
            'volume_avg': int(hist['Volume'].mean()),
            'volume_current': int(latest['Volume']),
            #make sure hist is long enough to calculate a price change
            'price_change_1d': round(latest['Close'] - hist.iloc[-2]['Close'], 2) if len(hist) > 1 else 0,
            'price_change_1w': round(latest['Close'] - week_ago['Close'], 2),
            'price_change_1m': round(latest['Close'] - month_ago['Close'], 2),
            #standard volatility calculation
            'volatility': round(hist['Close'].pct_change().std() * 100, 2)
        }

    #self explanatory: extracts key metrics from our ticker
    def _extract_financial_metrics(self, info):
        return {
            'pe_ratio': info.get('trailingPE', 'N/A'),
            'forward_pe': info.get('forwardPE', 'N/A'),
            'price_to_book': info.get('priceToBook', 'N/A'),
            'price_to_sales': info.get('priceToSalesTrailing12Months', 'N/A'),
            'dividend_yield': info.get('dividendYield', 'N/A'),
            'payout_ratio': info.get('payoutRatio', 'N/A'),
            'profit_margin': info.get('profitMargins', 'N/A'),
            'operating_margin': info.get('operatingMargins', 'N/A'),
            'return_on_equity': info.get('returnOnEquity', 'N/A'),
            'return_on_assets': info.get('returnOnAssets', 'N/A'),
            'debt_to_equity': info.get('debtToEquity', 'N/A'),
            'current_ratio': info.get('currentRatio', 'N/A'),
            'beta': info.get('beta', 'N/A')
        }

    def _calculate_technical_indicators(self, hist):
        """calculator for more techincial indicators, mainly just used pandas to calculate these
            moving averages and my functions to calculate RSI and MACD"""
        if hist.empty:
            return {}

        close_prices = hist['Close']

        # Moving averages
        sma_20 = close_prices.rolling(window=20).mean().iloc[-1] if len(close_prices) >= 20 else None
        sma_50 = close_prices.rolling(window=50).mean().iloc[-1] if len(close_prices) >= 50 else None
        sma_200 = close_prices.rolling(window=200).mean().iloc[-1] if len(close_prices) >= 200 else None

        # RSI calculation using defined method
        rsi = self._calculate_rsi(close_prices)

        # MACD using defined method
        macd, macd_signal = self._calculate_macd(close_prices)

        return {
            'sma_20': round(sma_20, 2) if sma_20 else 'N/A',
            'sma_50': round(sma_50, 2) if sma_50 else 'N/A',
            'sma_200': round(sma_200, 2) if sma_200 else 'N/A',
            'rsi': round(rsi, 2) if rsi else 'N/A',
            'macd': round(macd, 4) if macd else 'N/A',
            'macd_signal': round(macd_signal, 4) if macd_signal else 'N/A'
        }


    def _calculate_rsi(self, prices, period=14):
    """calculate relative strength index by gathering all the differences with pandas and computing gain
    and loss using these deltas."""
        if len(prices) < period + 1:
            return None

        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        #relative strength
        rs = gain / loss
        #rsi formula
        rsi = 100 - (100 / (1 + rs))
        return rsi.iloc[-1]

    def _calculate_macd(self, prices):
        """calculate MACD indicator using pandas built in ewm methods on our collected pricing data"""

        #make sure there is enough data to get the slow exponential moving average
        if len(prices) < 26:
            return None, None

        ema_12 = prices.ewm(span=12).mean()
        ema_26 = prices.ewm(span=26).mean()
        #standard formula
        macd_line = ema_12 - ema_26
        signal_line = macd_line.ewm(span=9).mean()

        return macd_line.iloc[-1], signal_line.iloc[-1]

    # organize all this collected data and metrics into one
    def analyze_stock(self, symbol):
        #make a nice-ish(not really) display while analyzing
        print(f"\n{'=' * 60}")
        print(f"ANALYZING: {symbol.upper()}")
        print(f"{'=' * 60}")

        data = self.get_comprehensive_data(symbol)
        #error handling
        if not data:
            print("Failed to retrieve data")
            return None

        #display results
        self._display_basic_info(data['basic_info'])
        self._display_price_data(data['price_data'])
        self._display_financial_metrics(data['financial_metrics'])
        self._display_technical_indicators(data['technical_indicators'])

        return data

    # print out basic company info and make sure to handle cases for missing data
    def _display_basic_info(self, info):
        print(f"\n📊 COMPANY INFO:")
        print(f"Company: {info['company_name']}")
        print(f"Sector: {info['sector']} | Industry: {info['industry']}")
        print(f"Country: {info['country']}")
        print(f"Employees: {info['employees']:,}" if info['employees'] != 'N/A' else "Employees: N/A")
        print(f"Market Cap: ${info['market_cap']:,.0f}" if info['market_cap'] != 'N/A' else "Market Cap: N/A")

    # for quick pricing information
    def _display_price_data(self, price_data):
        print(f"\n💰 PRICE DATA:")
        print(f"Current Price: ${price_data.get('current_price', 'N/A')}")
        print(f"52W High: ${price_data.get('high_52_week', 'N/A')} | 52W Low: ${price_data.get('low_52_week', 'N/A')}")
        print(f"1D Change: ${price_data.get('price_change_1d', 'N/A')}")
        print(f"1W Change: ${price_data.get('price_change_1w', 'N/A')}")
        print(f"1M Change: ${price_data.get('price_change_1m', 'N/A')}")
        print(f"Volatility: {price_data.get('volatility', 'N/A')}%")

    # for printing out financial metrics
    def _display_financial_metrics(self, metrics):
        """Display financial ratios"""
        print(f"\n📈 FINANCIAL METRICS:")
        print(f"P/E Ratio: {metrics.get('pe_ratio', 'N/A')}")
        print(f"P/B Ratio: {metrics.get('price_to_book', 'N/A')}")
        print(f"Dividend Yield: {metrics.get('dividend_yield', 'N/A')}")
        print(f"ROE: {metrics.get('return_on_equity', 'N/A')}")
        print(f"Debt/Equity: {metrics.get('debt_to_equity', 'N/A')}")
        print(f"Beta: {metrics.get('beta', 'N/A')}")

    # for printing out all the technical indicators
    def _display_technical_indicators(self, indicators):
        """Display technical analysis"""
        print(f"\n🔍 TECHNICAL INDICATORS:")
        print(f"20-day SMA: ${indicators.get('sma_20', 'N/A')}")
        print(f"50-day SMA: ${indicators.get('sma_50', 'N/A')}")
        print(f"RSI: {indicators.get('rsi', 'N/A')}")
        print(f"MACD: {indicators.get('macd', 'N/A')}")

    # compare multiple stocks side by side
    def compare_stocks(self, symbols):
        print(f"\n{'=' * 80}")
        print(f"STOCK COMPARISON")
        print(f"{'=' * 80}")

        comparison_data = []
        for symbol in symbols:
            data = self.get_comprehensive_data(symbol)
            if data:
                comparison_data.append({
                    'Symbol': symbol.upper(),
                    'Price': data['price_data'].get('current_price', 'N/A'),
                    'P/E': data['financial_metrics'].get('pe_ratio', 'N/A'),
                    'Market Cap': data['basic_info'].get('market_cap', 'N/A'),
                    'ROE': data['financial_metrics'].get('return_on_equity', 'N/A'),
                    '1M Change': data['price_data'].get('price_change_1m', 'N/A')
                })

        #make sure there is data to display, then convert data into pandas data frame, then print it
        if comparison_data:
            df = pd.DataFrame(comparison_data)
            print(df.to_string(index=False))

        return comparison_data

#mode for user input
def interactive_mode():
    analyzer = AdvancedStockAnalyzer()

    print("🚀 Advanced Stock Analyzer")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Analyze single stock")
        print("2. Compare multiple stocks")
        print("3. Quick price check")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            symbol = input("Enter stock symbol (e.g., AAPL): ").strip().upper()
            if symbol:
                analyzer.analyze_stock(symbol)

        elif choice == "2":
            symbols_input = input("Enter stock symbols separated by commas (e.g., AAPL,GOOGL,MSFT): ")
            #split up the tokens and then input into the comparison method
            symbols = [s.strip().upper() for s in symbols_input.split(",") if s.strip()]
            if symbols:
                analyzer.compare_stocks(symbols)

        elif choice == "3":
            symbol = input("Enter stock symbol for quick price: ").strip().upper()
            if symbol:
                try:
                    #just manually do it so you don't have to look up all the other data
                    ticker = yf.Ticker(symbol)
                    price = ticker.history(period="1d")['Close'].iloc[-1]
                    print(f"{symbol}: ${price:.2f}")
                except:
                    print(f"Could not fetch price for {symbol}")

        elif choice == "4":
            print("Quitting stock analyzer.")
            break

        else:
            print("Try entering another key.")


def main():
    analyzer = AdvancedStockAnalyzer()

    print("🚀 Stock Data Analyzer Demo")
    print("Analyzing Apple (AAPL)...")

    analyzer.analyze_stock("AAPL")

    print("\n" + "=" * 60)
    print("Want to try interactive mode? (y/n): ", end="")

    if input().lower() == 'y':
        interactive_mode()


if __name__ == "__main__":
    main()