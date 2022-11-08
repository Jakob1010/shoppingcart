import unittest

from shopping_cart import ShoppingCartConcreteCreator
from test_utils import Capturing
from receipt_format import ReceiptFormat

class ShoppingCartAddItemTest(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCartConcreteCreator().operation()
        self.cart.add_item("apple", 2)

    def test_add_single_item(self):
        self.assertEqual(self.cart.items,["apple"])
        self.assertEqual(self.cart.items_quantity, {"apple": 2})

    def test_add_multiple_items(self):
        self.cart.add_item("banana", 3)
        self.assertEqual(self.cart.items,["apple", "banana"])
        self.assertEqual(self.cart.items_quantity, {"apple": 2, "banana": 3})

    def test_update_item(self):
        self.cart.add_item("apple", 3)
        self.assertEqual(self.cart.items,["apple"])
        self.assertEqual(self.cart.items_quantity, {"apple": 5})


class ShoppingCartReceiptTest(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCartConcreteCreator().operation()
        self.cart.add_item("apple", 2)

    def test_print_receipt(self):
        with Capturing() as output:
            self.cart.print_receipt()
        price = self.cart.pricer.get_price("apple")
        line = self.cart.receipt_format.get_line("apple", 2, price)
        self.assertEqual(line, output[0])

    def test_doesnt_explode_on_mystery_item(self):
        self.cart.add_item("pear", 5)
        with Capturing() as output:
            self.cart.print_receipt()
        price_apple = self.cart.pricer.get_price("apple")
        self.assertEqual(f"apple - 2 - {price_apple}", output[0])
        self.assertEqual("pear - 5 - 0", output[1])

    def test_print_total_price(self):
        self.cart.add_item("banana", 5)  
        with Capturing() as output:
            self.cart.print_receipt()      
        price_apple = self.cart.pricer.get_price("apple")
        price_banana = self.cart.pricer.get_price("banana")
        total = price_apple * 2 + price_banana * 5
        self.assertEqual(f"Total: {total}", output[-1])

    def test_print_total_with_update(self):
        self.cart.add_item("apple", 2)
        with Capturing() as output:
            self.cart.print_receipt()      
        price_apple = self.cart.pricer.get_price("apple")
        total = price_apple * 4
        self.assertEqual(f"Total: {total}", output[-1])        

    def test_print_price_first_format(self):
        self.cart = ShoppingCartConcreteCreator().operation(1)
        self.cart.add_item("banana", 5)
        with Capturing() as output:
            self.cart.print_receipt()    
        price_banana = self.cart.pricer.get_price("banana")
        self.assertEqual(f"{price_banana} - banana - 5", output[0])        



unittest.main(exit=False)
