import functools
numbers = [120, 30, 54, 36]
print(functools.reduce(lambda x, y: x-y, numbers))
