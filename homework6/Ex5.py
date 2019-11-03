employees = {}
print("Enter the number of employees: ")
num = int(input())
for i in range(num):
    print("Enter the name of the employee: ")
    name = input()
    print("Enter the salary of the employee: ")
    salary = input()
    employees[name] = salary

for employee in employees:
    print(employees)
print("-----------------------------------------------------------")

values = list(employees.values())
print(max(values))
print(min(values))
