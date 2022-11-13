from enum import Enum

class Format(Enum):
    DEFAULT = 0
    PRICE_FIRST = 1


class ReceiptFormat:
    """
    Defines format of receipt.
    ---------
    Params:
        - format: Id of format. 
    """
    def __init__(self, format):
        self.format = format

    def get_line(self, item, quantity, price):
        if self.format == Format.DEFAULT:
            return (f"{item} - {quantity} - {price}")
        elif self.format == Format.PRICE_FIRST:
            return (f"{price} - {item} - {quantity}")
        else:
            return 'invalid receipt format'
