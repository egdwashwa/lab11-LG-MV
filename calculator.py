# https://github.com/<git@github.com:egdwashwa/lab11-LG-MV.git>
# Partner 1: <Leon Grigoruk>
# Partner 2: <Megan Vu>
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
def square_root(a):
    if a < 0:
        raise ValueError 
    math.sqrt(a)
def hypotenuse(a, b): 
    math.hypot(a, b)

def add(a, b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def log(a,b):
    if a <= 0 or a==1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(a,b)
    
def exp(a, b):
    return a**b
