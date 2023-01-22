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

def abs(x = 1):
    if (x < 0):
        x = x * -1
        return (x)
    else:
        return(x)

def subs(x = 1, y = 1):
    subeq = sub(x, y)
    return subeq

def lim(c = 2, x = 1, y = 1, z = 0):
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

def dif(x = 1, y = 1, z = 1):
    #x = expression
    #y = the term being differentiated
    #z = number of diff

    ysymb = symbols(y)

    differ = diff(x, ysymb, z)
    return differ


def inte(c = 0, x = 1 , y = 1, a = 1, b = 1):
    #c == 0 => integration without limits
    #c == 1 => integration with limits
    #x = expression
    #y = reference variable
    #a = lower limit
    #b = upper limit

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
print("Use Ctrl+C at any time to exit the calculator\n")
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

def operations():
    choice = int(input("Choose an operation by entering its preceding number: "))
    return choice

i = 1

while (i == 1):
    cho = operations()
    print("Note: The default input value of most of these operations is 1 \n")
    if (cho >= 0) and (cho <= 6):
        if (cho == 0):
            a1 = float(input("Enter first number to be added: "))
            b1 = float(input("Enter second number to be added: "))
            e1 = add(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 1):
            a1 = float(input("Enter the first number to be subtracted from: "))
            b1 = float(input("Enter the second number to subtract: "))
            e1 = sub(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 2):
            a1 = float(input("Enter first number: "))
            b1 = float(input("Enter second number: "))
            e1 = mult(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 3):
            a1 = float(input("Enter Dividend: "))
            b1 = float(input("Enter Divisor: "))
            e1 = div(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 4):
            a1 = float(input("Enter Dividend: "))
            b1 = float(input("Enter Divisor: "))
            e1 = floor_div(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 5):
            a1 = float(input("Enter Dividend: "))
            b1 = float(input("Enter Divisor: "))
            e1 = mod(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 6):
            a1 = float(input("Enter Base: "))
            b1 = float(input("Enter Exponent: "))
            e1 = exp(a1, b1)
            print("The result is: ", e1, "\n")
    elif (cho >= 7) and (cho <= 11):
        if (cho == 7):
            a1 = float(input("Enter Number: "))
            e1 = abs(a1)
            print("The result is: ", e1, "\n")
        elif (cho == 8):
            a1 = input("Enter Expression in terms of x: ")
            b1 = float(input("Enter value to substitute with: "))
            e1 = subs(a1, b1)
            print("The result is: ", e1, "\n")
        elif (cho == 9):
            chi = int(input("Enter 0 for Right Hand Limit, 1 for Left Hand Limit and 2 for Evaluating a Limit: "))
            a1 = input("Enter Expression of Limit to be Evaluated: ")
            b1 = input("Enter the primary variable of the limit: ")
            c1 = input("Enter what the primary limit tends to (Note: Use oo (double o) for infinity): ")
            e1 = lim(chi, a1, b1, c1)
            pretty_print(print("The Limit Evaluates to:", e1))
        elif (cho == 10): 
            a1 = input("Enter expression to be differentiated: ")
            b1 = input("Enter differentiating term/differentiating with respect to: ")
            c1 = int(input("Enter number of times to differentiate (Enter 1 for single differentiation): "))
            e1 = dif(a1, b1, c1)
            pretty_print(print("The Derivative is:", e1))
        elif (cho == 11):
            chi = int(input("Enter 0 for integration without limits and 1 for integration with limits: "))
            if (chi == 0):
                a1 = input("Enter Expression to be Integrated: ")
                b1 = input("Enter Integrating Variable/Integrating with respect to: ")
                e1 = inte(chi, a1, b1)
            elif (chi == 1):
                a1 = input("Enter Expression to be Integrated: ")
                b1 = input("Enter Integrating Variable/Integrating with respect to: ")
                c1 = input("Enter Lower Limit (Note: Use oo (double o) for infinity): ")
                d1 = input("Enter Upper Limit (Note: Use oo (double o) for infinity): ")
                e1 = inte(chi, a1, b1, c1, d1)
            else:
                print("Invalid Response")
            pretty_print(print("The Result after Integration is:", e1))
    else:
        print("Invalid Response")
        continue