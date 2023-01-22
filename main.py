#importing

from sympy import symbols, limit

#calculator operations as functions

def add(x = 1, y = 1):
    return (x+y)

def sub(x = 1, y = 1):
    return (x-y)

def mult(x = 1, y = 1):
    return (x*y)

def div(x = 1, y = 1):
    return (x/y)

def floor_div(x = 1, y = 1):
    return (x//y)

def mod(x = 1, y = 1):
    return (x%y)

def exp(x = 1, y = 1):
    return (x**y)

def abs(x):
    if (x < 0):
        x = x * -1
        return (x)
    else:
        return(x)

def lim():
    print("placeholder")

def dif():
    print("placeholder")

def inte():
    print("placeholder")

#inputs for operation

print("\nWelcome to a 'Simple' Calculator!\nThis Calculator is completely made in Python and supports 11 different operations!\n")

print("0 - Addition")
print("1 - Subtraction")
print("2 - Multiplication")
print("3 - Division (Returns Quotient)")
print("4 - Floor Division (Returns only the Integral Part of the Quotient)")
print("5 - Modulus (Returns Remainder)")
print("6 - Exponent (Performs an Exponential Operation on two numbers)")
print("7 - Absolute Value (Returns Magnitude)")
print("8 - Limits (Performs a Limit Operation)")
print("9 - Differentiation (Performs a Differentiation Operation on a single term)")
print("10 - Integration (Performs an Integration Operation on a single term)\n")

o = int(input("hold"))