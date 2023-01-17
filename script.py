# property of Jason Diaz (drxjason on GitHub)

import math
import colorama
from termcolor import colored

colorama.init()
number = int(input("enter a number to factor perfectly: "))

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def check_decimal(x):
    if x != int(x):
        return str(x) + " <- Improper Factor"

    else:
        return colored(f"{str(int(x))} <- Perfect Square Factor", "yellow")   

for i in squares:
    print(f"square {str(i)}: {str(check_decimal(number/i))}")
