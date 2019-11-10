numbers = []
print("Input numbers: ")
for num in range(6):
    num_input = int(input())
    numbers.append(num_input)

def pos_divbysix(numbers):
    count = 0
    for num in numbers:
        if num > 0 and num % 6 == 0:
            count += 1
    print("There are: {0} positive and dividable by six number/s".format(count))

def odd_numbers(numbers):
    new_list = [num for num in numbers if num%2!=0]
    print("There are {0} odd numbers in the list: {1}".format(len(new_list), new_list))


pos_divbysix(numbers)
odd_numbers(numbers)

