files = {'text.txt': 15, 'word': 20, 'anatomy.txt': 15, 'artificial': 25}
count1 = 0
count2 = 0

keys = list(files.keys())
values = list(files.values())

for key in keys:
    if files[key] > 15:
        count1 += 1
    if key[0] == 'a' and key[-4:] == '.txt':
        count2 += 1
        files[key] += 20
print("Greater than 15: ", count1)
print("Starts with 'a' and ends with '.txt': ", count2)
for i in files.keys():
    print(files[i])

