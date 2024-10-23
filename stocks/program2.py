import csv
from dataclasses import dataclass
from datastructures.intervaltree import IntervalTree

@dataclass(order=True)
class Stock:
    symbol: str
    name: str
    low: int
    high: int

class StockManager:
    def __init__(self):
        self._interval_tree = IntervalTree()

    def add_stock(self, stock: Stock):
        self._interval_tree.insert(stock.low, stock.high, stock)

    def load_from_csv(self, filepath):
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            for row in reader:
                symbol, name, low, high = row[0], row[1], int(row[2]), int(row[3])
                stock = Stock(symbol, name, low, high)
                self.add_stock(stock)

    def display_all_stocks(self):
        stocks = self._interval_tree.inorder()  # Assuming 'inorder' returns a list of stocks
        for stock in stocks:
            print(f"{stock.symbol} - {stock.name} - {stock.low}-{stock.high}")

def main():
    stock_manager = StockManager()
    stock_manager.load_from_csv('sample_stock_prices.csv')  # Load stocks from CSV
    stock_manager.display_all_stocks()  # Display all loaded stocks

if __name__ == "__main__":
    main()
