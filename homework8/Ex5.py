flowers = {'rose': 'red', 'lily': 'white', 'tulip': 'red', 'orchids': 'purple'}
values = list(flowers.values())
print(list(filter(lambda x: x == 'red', values)))
