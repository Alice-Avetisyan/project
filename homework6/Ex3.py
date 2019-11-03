company1 = {'Alex', 'Anna', 'Chris', 'Josh', 'Emma'}
company2 = {'Greg', 'Anna', 'Karen', 'Lenny', 'Emma'}
print("-----------------------------------------------------------")
print("Working for both companies: ", company1 | company2)
print("-----------------------------------------------------------")
print("Employees working in both companies: ", company1 & company2)
print("-----------------------------------------------------------")
print("Enter an employee's name: ")

name_in = input()
for name1 in company1:
    if name_in == name1:
        print("Company 1: ", name1)

for name2 in company2:
    if name_in == name2:
        print("Company 2:", name2)
