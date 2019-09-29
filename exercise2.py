from math import sqrt, factorial
from random import randint

# Ex1
print("-----Exercise 1-----")
print("Please enter the first float number: ")
num1 = float(input())
print("Please enter the second float number: ")
num2 = float(input())
print("Please enter the third float number: ")
num3 = float(input())
numsum = num1 + num2 + num3
print("The sum is: ", numsum)

# Ex2
print("-----Exercise 2-----")
print("Please enter the first integer number: ")
num4 = int(input())
print("Please enter the second integer number: ")
num5 = int(input())
ratio = int(num4/num5)
print("The answer is: ", ratio)

# Ex3
print("-----Exercise 3-----")
print("Please enter the first positive or negative number: ")
num6 = int(input())
print("Please enter the second positive or negative number: ")
num7 = int(input())
if(num6 > 0 and num7 > 0):
    print("Your numbers are positive")
else:
    print("One or more number is negative")

# Ex4
print("-----Exercise 4-----")
print("(Symbol or no symbol) Please enter a number: ")
num8 = input()
if(num8 == ""):
    print("No symbols")
else:
    print("Contains symbols")

# Ex5
print("-----Exercise 5-----")
print("Please enter a number: ")
num9 = int(input())
if(num9 > 0):
    print("The square root of your inputed number is:", sqrt(num9))
else:
    print("Please input a positive number")

# Ex6
print("-----Exercise 6-----")
print("Please enter the first integer number: ")
num10 = int(input())
print("Please enter the second float number: ")
num11 = float(input())
sumnum = num10 + num11
strconc = str(num10) + str(num11)
print("The sum is:", sumnum, "The concatenation is: ", strconc)

# Ex7
print("-----Exercise 7-----")
print("Random number")
randnum = randint(1, 100)
if(randnum > 15 and randnum < 36):
    print("Ture. Your number is:", randnum)
else:
    print("Flase. Your number is:", randnum)

# Ex8
print("-----Exercise 8-----")
print("(Factorial) Please enter an integer number: ")
num12 = int(input())
numfact = factorial(num12)
if(numfact > 0 and numfact < 100):
    print("True. The factorial of your number is:", numfact)
else:
    print("False. The factorial of your is:", numfact)




