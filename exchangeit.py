"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Sanam Maharjan
Date:   June 8th, 2025
"""

import currency
from currency import exchange

# for input
src = input("3-letter code for original currency: ")
dst = input("3-letter code for the new currency: ")
amt = float(input("Amount of the original currency: "))

# conversion 
converted_amount = exchange(src, dst, amt)

print(f"You can exchange {amt} {src.upper()} for {converted_amount:.3f} {dst.upper()}.")


