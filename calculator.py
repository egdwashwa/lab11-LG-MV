import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
<<<<<<< HEAD
# First example
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

def exp(a,b):
    return a ** b

import math
def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def log(a, b):
    if a<=0 or b<=0:
        raise ValueError
    return math.log(a,b)
    
def exp(a, b):
    return a**b
