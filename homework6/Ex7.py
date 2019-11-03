numbers = []
print("Enter 7 numbers:")
for i in range(7):
    num_inp = int(input())
    numbers.append(num_inp)

for i in range(len(numbers)):
    if i != 0:
        if numbers[i] > numbers[i-1]:
            print(numbers[i])
    else:
        print(numbers[0])
