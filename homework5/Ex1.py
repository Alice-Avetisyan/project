old_list = [2, 4, 29, 60, 57, 39]
new_list = [num for num in old_list if num % 2 != 0 or num % 6 == 0]
print(new_list)
