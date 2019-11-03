from math import sqrt
numbers = []
print("Enter numbers: ")
for num in range(6):
    num_inp = int(input())
    numbers.append(num_inp)
print(numbers)
print("-----------------------------------------------------------")
for number in numbers:
    if sqrt(number) < 26:
        print(number)
        break
