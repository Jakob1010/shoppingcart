from abc import ABC, abstractmethod

from shopping_cart_interface import IShoppingCart
from pricer import Pricer


class ShoppingCart(IShoppingCart):
    """
    Implementation of the shopping tills in our supermarket.
    """
    def __init__(self, pricer: Pricer, recipe_format=0):
        self.pricer = pricer
        self.items = []
        self.items_quantity = {}
        self.recipe_format = recipe_format


    def add_item(self, item_type: str, number: int):
        if item_type not in self.items_quantity:
            self.items.append(item_type)
            self.items_quantity[item_type] = number
        else:
            self.items_quantity[item_type] += number


    def print_receipt(self):
        total = 0

        for item in self.items:
            quantity = self.items_quantity[item]
            price = self.pricer.get_price(item)
            total += quantity * price

            if self.recipe_format == 0:
                print(f"{item} - {quantity} - {price}")
            else:
                print(f"{price} - {item} - {quantity}")

        print("Total: {total}".format(total=total))


class ShoppingCartCreator(ABC):
    """
    Interface for the ShoppingCart creator.
    The creation process will be delegated to the subclasses of this class.
    """
    @abstractmethod
    def factory_method(self) -> ShoppingCart:
        # return the ShoppingCart object
        pass

    def operation(self) -> ShoppingCart:
        # Here more operations can be performed on the ShoppingCart object
        # returns ShoppingCart object
        return self.factory_method()


class ShoppingCartConcreteCreator(ShoppingCartCreator):
    """
    Concrete class for the ShoppingCart creator.
    Implements the factory_method
    """

    def factory_method(self) -> ShoppingCart:
        # returns ShoppingCart object
        return ShoppingCart(Pricer())
