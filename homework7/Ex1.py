numbers1 = []
numbers2 = []
numbers3 = []

print("Enter numbers for the first collection: ")
for num_in1 in range(6):
    number_inp1 = int(input())
    numbers1.append(number_inp1)

print("Enter numbers for the second collection: ")
for num_in2 in range(6):
    number_inp2 = int(input())
    numbers2.append(number_inp2)

print("Enter numbers for the third collection: ")
for num_in3 in range(6):
    number_inp3 = int(input())
    numbers3.append(number_inp3)

string = """1. Greater than 10
2. Greater than 20
3. Greater than 30"""

print("Please, choose from the given options: (1, 2 or 3)")
print(string)
print("Your choice: ")
inp_choice = int(input())

count = 0
if inp_choice == 1:
    for num1 in numbers1:
        if num1 > 10:
            count += 1
elif inp_choice == 2:
    for num2 in numbers2:
        if num2 > 20:
            count += 1
elif inp_choice == 3:
    for num3 in numbers3:
        if num3 > 30:
            count += 1
else:
    print("Stoping the program")
print("This is the quantity of numbers without use of a function: ", count)

def count_numbers(numbers1,numbers2,numbers3, inp_choice):
    count = 0

    if inp_choice == 1:
        for num1 in numbers1:
            if num1 > 10:
                count += 1
    elif inp_choice == 2:
        for num2 in numbers2:
            if num2 > 20:
                count += 1
    elif inp_choice == 3:
        for num3 in numbers3:
            if num3 > 30:
                count += 1
    print("This is the quantity of numbers with a function: ", count)

print("------------------------------------------------------------")
count_numbers(numbers1, numbers2, numbers3, inp_choice)

