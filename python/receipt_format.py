class ReceiptFormat:
    """
    Defines format for receipt.
    """
    def __init__(self,receipt_format):
        self.receipt_format = receipt_format

    def get_receipt_line(self, item, quantity, price):
        """ Returns a single line of a receipt according to the defined format. """
        if self.receipt_format == 0:
            return (f"{item} - {quantity} - {price}")
        else:
            return (f"{price} - {item} - {quantity}")
