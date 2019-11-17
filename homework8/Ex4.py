numbers1 = []
numbers2 = []

print("Enter numbers for the first collection: ")
for num1 in range(6):
    num1_inp = int(input())
    numbers1.append(num1_inp)

print("Enter numbers for the second collection: ")
for num2 in range(6):
    num2_inp = int(input())
    numbers2.append(num2_inp)

print("First collection: ", numbers1)
print("Second collection: ", numbers2)

print(list(map(lambda x, y: x**2 + y**2, numbers1, numbers2)))


