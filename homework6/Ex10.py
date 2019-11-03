print("Enter the first number: ")
number = int(input())

prod = 1
numbers = range(0, number)
for num in numbers:
    if num == 0:
        continue
    prod *= num
print(prod)