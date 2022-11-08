class ReceiptFormat:
    """
    Defines format for receipt.
    """
    def __init__(self,receipt_format):
        # right now only two formats are supported
        if receipt_format not in [0,1]:
            receipt_format = 0
        self.receipt_format = receipt_format

    def get_line(self, item, quantity, price):
        """ Returns a single line of a receipt according to the defined format. """
        if self.receipt_format == 0:
            return (f"{item} - {quantity} - {price}")
        elif self.receipt_format == 1:
            return (f"{price} - {item} - {quantity}")
        else:
            return 'invalid receipt format'
