prices = [50, 24, 95, 42, -20, 500]
sum = 0
for num in prices:
    if num < 0:
        break
    sum += num
print(sum)


