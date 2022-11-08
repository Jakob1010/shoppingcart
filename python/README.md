# Background

This repository is a take home assignments. The original code is taken from here: [github.com](https://github.com/jbanother/shoppingcart)

# What was done

## Add a 'Total' line to the receipt
For this, the **print_receipt()** function in **shopping_car.py** was updated. During the print process a variable called 'total' keeps track of the total price.

## Make the receipt print items in the order that they were scanned
In order to preserve the scan order for the receipt, the data structure was changed to a list for the item names (which naturally keeps track of the order) and a hashmap for the quantity of each item. Here it assumed that when an item is updated the order of an item is based on its first scan. 
With this approach both add_item() and print_receipt() can run in **O(n)**. 

## Allow different receipt format
A new class **'receipt_format.py'** that takes differnt formatting codes (0,1) and automatically applies the correct format in **get_line()**

## Update test suite
New tests were added in order to verify the changes made. Also **setUp** was used to minimize the number of tests that need to be udpated when changes for the shopping_cart class are made.
