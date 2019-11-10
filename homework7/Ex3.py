employees = {'Jack Smith': 'Engineer', 'Hideo Kojima': 'Director', 'Yoji Shinkawa': 'Art_director', 'John Anderson': 'Engineer'}

def find_employee(employees):
    keys = list(employees.keys())
    count = 0
    for key in keys:
        if key[:4] == 'John':
            count += 1
    print("There is/are {0} employee/s with the name John".format(count))

def find_engineer(employees):
    values = list(employees.values())
    count = 0
    for value in values:
        if value == 'Engineer':
            count += 1
    print("There is/are {0} employee/s with the Engineer position".format(count))

find_employee(employees)
find_engineer(employees)