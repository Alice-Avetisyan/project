pets = {'cat': 'Johny', 'dog': 'Rex', 'parrot': 'Jack', 'mouse': 'Johny'}
count = 0
values = list(pets.values())
for value in values:
    if value == 'Johny':
        count += 1
print(count)
