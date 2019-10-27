students = {}

for i in range(2):
    print("Enter the student's name")
    name = input()
    print("Enter the student's score")
    score = int(input())
    students[name] = score

print(students)

keys = list(students.keys())
for key in keys:
    if students[key] < 40:
        students.pop(key)
print(students)
