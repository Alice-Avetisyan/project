print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())

prod = 1
numbers = range(num1, num2)
for num in numbers:
    prod *= num
print(prod)
