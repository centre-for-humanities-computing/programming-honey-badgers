"""
Illustration of data classes,  decorator and functions for 
automatically adding generated special methods 
such as __init__() and __repr__() to user-defined classes.
"""
from dataclasses import dataclass


@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory"""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


def main():
    item = InventoryItem(name='penguin', unit_price=5, quantity_on_hand=3)
    print(item.total_cost())


if __name__ == '__main__':
    main()