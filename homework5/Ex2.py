names = []
print("Input 6 names: ")
for inname in range(6):
    namein = input()
    names.append(namein)

new_list = [name for name in names if name[0] == 'A']
print(new_list)