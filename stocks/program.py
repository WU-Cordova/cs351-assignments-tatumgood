from dataclasses import dataclass
from typing import List, Optional
from datastructures.intervaltree import IntervalTree
#from datastructures.avltree import AVLTree

@dataclass(order=True)
class Stock:
    symbol: str
    name: str
    low: int
    high: int
    current_price: float

class StockManager:
    def __init__(self):
        self._interval_tree = IntervalTree()
        self._price_history = {}

    def add_stock(self, stock: Stock):
        self._interval_tree.insert(stock.low, stock.high, stock)

    def update_stock(self, symbol: str, new_low: int, new_high: int):
        stock = self.find_stock_by_symbol(symbol)
        if stock:
            self._interval_tree.delete(stock.low, stock.high)
            stock.low = new_low
            stock.high = new_high
            self._interval_tree.insert(new_low, new_high, stock)

    def delete_stock(self, symbol: str):
        stock = self.find_stock_by_symbol(symbol)
        if stock:
            self._interval_tree.delete(stock.low, stock.high)

    def lookup_stock_price(self, symbol: str) -> Optional[float]:
        stock = self.find_stock_by_symbol(symbol)
        return stock.current_price if stock else None

    # def get_top_k_stocks(self, k: int) -> List[Stock]:
    #     stocks = self._interval_tree.inorder()
    #     return sorted(stocks, key=lambda x: x.value.high, reverse=True)[:k]

    def get_top_k_stocks(self, k: int):
        stock_keys = self._interval_tree.inorder()  # This gets the interval tree keys (low values)
        
        stocks = []
        for key in stock_keys:
            stock_node = self._interval_tree._tree.search(key)  # Search for the IntervalNode using the key
            if stock_node:
                stocks.append(stock_node.value)  # Append the Stock object from the IntervalNode's value

        # Sort the stocks by their high value and return the top k stocks
        return sorted(stocks, key=lambda stock: stock.high, reverse=True)[:k]


    def get_bottom_k_stocks(self, k: int) -> List[Stock]:
        stocks = self._interval_tree.inorder()
        return sorted(stocks, key=lambda x: x.value.low)[:k]

    def get_stocks_in_price_range(self, low: int, high: int) -> List[Stock]:
        return self._interval_tree.range_query(low, high)

    def track_price(self, symbol: str, price: float):
        if symbol not in self._price_history:
            self._price_history[symbol] = []
        self._price_history[symbol].append(price)

    def generate_alert(self, symbol: str, threshold: float):
        stock = self.find_stock_by_symbol(symbol)
        if stock and stock.current_price >= threshold:
            print(f"Alert: {stock.symbol} has crossed the price threshold of {threshold}.")

    # def find_stock_by_symbol(self, symbol: str) -> Optional[Stock]:
    #     stocks = self._interval_tree.inorder()
    #     for stock in stocks:
    #         if stock.value.symbol == symbol:
    #             return stock.value
    #     return None
    
    def find_stock_by_symbol(self, symbol: str):
        stock_keys = self._interval_tree.inorder()  # Get the keys (price intervals)

        for key in stock_keys:
            stock_node = self._interval_tree._tree.search(key)  # Get the IntervalNode object
            if stock_node and stock_node.value.symbol == symbol:
                return stock_node.value  # Return the Stock object
        return None


def main():
    stock_manager = StockManager()
    stock_manager.add_stock(Stock('AAPL', 'Apple Inc.', 120, 150, 135))
    stock_manager.add_stock(Stock('GOOGL', 'Alphabet Inc.', 173, 213, 190))

    print(stock_manager.lookup_stock_price('AAPL'))  # Output: 135

    stock_manager.update_stock('AAPL', 130, 160)
    print(stock_manager.lookup_stock_price('AAPL'))  # Updated price

    top_stock = stock_manager.get_top_k_stocks(1)
    print(f"Top Stock: {top_stock}")

    stocks_in_range = stock_manager.get_stocks_in_price_range(100, 200)
    print(f"Stocks in Range: {stocks_in_range}")

    stock_manager.track_price('GOOGL', 215)
    stock_manager.generate_alert('GOOGL', 210)

if __name__ == "__main__":
    main()


