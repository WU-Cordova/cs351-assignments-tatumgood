from dataclasses import dataclass
from datastructures.avltree import AVLTree
from datastructures.intervaltree import IntervalTree

@dataclass(order=True)
class Stock:
    symbol: str 
    name: str
    low: int
    high: int
    #price: float 

class StockManager:
    def __init__(self):
        self._interval_tree = IntervalTree()

        stocks = [ 
            Stock('GOOGL', 'Alphabet Inc.', '173', '213')
        ]

def main():
    tree = AVLTree()
    print("Hello, world!")

if __name__ == "__main__":
    main()