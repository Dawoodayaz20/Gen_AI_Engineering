Module:
A module is a Python file that contains functions, classes, or variables. You can import it into other Python files to reuse its code. It allows you to divide your program into smaller, manageable pieces.
Creating a Module:
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

Using the Module in Another File:
# main.py
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8

There are many usages of modules in python: 
import math : In this case, you import the entire math module and can use its functions with the math. prefix.

import module1, module2, module3 :
import module1, module2, module3
# Example usage (assuming the modules have relevant functions)
module1.function1()
module2.function2()
module3.function3()

If i want to use one or more function from a module in another file, i will have to write :
from maths_functions import sin, pi, cos

from math import sin as sine_funct:
You are importing the sin function and giving it an alias sine_funct, so you can use the alias instead of sin. 