from math import factorial
numbers = []
print("Enter 3 numbers: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

print(factorial(numbers[-1]))