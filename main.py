#importing

from sympy import symbols, limit, cos, sin, tan, cot, sec, csc, diff, integrate, oo, pretty_print

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

def subs(x, y):
    subeq = sub(x, y)
    return subeq

def lim(c, x, y, z = 0):
    #x = expression/term
    #y = variable/symbol
    #z value/tending to

    ysymb = symbols(y)

    if (c == 0):
        limt = limit(x, ysymb, z, "+")
        return limt
    elif (c == 1):
        limt = limit(x, ysymb, z, "-")
        return limt
    elif (c == 2):
        limt = limit(x, ysymb, z)
        return limt
    else:
        print("Invalid Response")

def dif(x, y, z = 1):
    #x = to see which dif operation
    #y = the term being differentiated
    #z = number of diff

    ysymb = symbols(y)

    differ = diff(x, ysymb, z)
    return differ


def inte(c, x , y, a = 1, b = 1):
    #c == 0 => integration without limits
    #c == 1 => integration with limits
    #x = expression
    #y = reference variable
    #a = upper limit
    #b = lower limit

    ysymb = symbols(y)
    
    if (c == 0):
        integ = integrate(x, ysymb)
        return integ
    elif (c == 1):
        integ = integrate(x, (ysymb, a, b))
        return integ
    else:
        print("Invalid Response")

#inputs for operation

print("\nWelcome to a 'Simple' Calculator!\nThis Calculator is completely made in Python and supports 12 different operations!\n")

print("0 - Addition")
print("1 - Subtraction")
print("2 - Multiplication")
print("3 - Division (Returns Quotient)")
print("4 - Floor Division (Returns only the Integral Part of the Quotient)")
print("5 - Modulus (Returns Remainder)")
print("6 - Exponent (Performs an Exponential Operation on two numbers)")
print("7 - Absolute Value (Returns Magnitude)")
print("8 - Algebraic Solver")
print("9 - Limits (Performs a Limit Operation)")
print("10 - Differentiation (Performs a Differentiation Operation on a single term)")
print("11 - Integration (Performs an Integration Operation on a single term)\n")

o = int(input("hold"))