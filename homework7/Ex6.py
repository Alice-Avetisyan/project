numbers = []

print("How many numbers would you like to input? ")
num = int(input())
print("Enter your number/s")
if num <= 1:
    number_inp = int(input())
    numbers.append(number_inp)
else:
    for number in range(num):
        number_inp = int(input())
        numbers.append(number_inp)

def inputed_numbers(numbers):
    print("Inputed numbers: ")
    for num in numbers:
        print(num)

    num_pow(2, numbers)
    even_numbers(numbers)

def num_pow(power, numbers):
    print("Calculate different power for inputed numbers: ")
    for num in numbers:
        print(num**power)

def greater_than_numbers(comparison_num, *number):
    print("Calculate how many numbers are greater than some specific number: ")
    count = 0
    for num in number:
        if num > comparison_num:
            count += 1
    print("{0} is/are greater than {1}".format(count, comparison_num))

def even_numbers(numbers):
    print("Calculate how many numbers are even")
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print("Even numbers: ", count)

def greater_than_pow(*number):
    print("Get number which power 3 is greater than 100: ")
    for num in number:
        if num**3 > 100:
            print(num)

print("Using inputed from console numbers: ")
inputed_numbers(numbers)
print("Using * symbol to 'input' more than one number: ")
greater_than_numbers(10, 4, 20, 2, 50)
greater_than_pow(20, 50, 12, 45)
