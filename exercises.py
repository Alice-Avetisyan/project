from math import sqrt
from random import choice
# ex1
a = 6
b = 2
print('(a+b)^2 =', (a+b)**2)

# ex2
loan = 1500
rate = 0.16
interest = loan * rate
payment = loan + interest * rate
print('This is how much we should pay:', payment)

# ex3
x = 5
y = 5
c = (x**2)+(y**2)
print('Hypotenuse is calculated using Pythagoras Theorem:', sqrt(c))

# ex4
print('Enter your name: ')
name = input()
print('Hi', name)

# ex5(6)
print('Enter a number: ')
num = int(input())
s = sqrt(num)
print('The square root of ', num, 'is:', s)

# ex6(7)
print('Hi ', name)
print('You are ', choice([3, 28, 100]), 'years old')
