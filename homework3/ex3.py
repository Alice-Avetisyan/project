from random import randint
numbers = [1, 20, 45, 60, 12, 4, 6]
print("Input a threshold: ")
threshold = int(input())
randomnum = randint(0, len(numbers)-1)
print(numbers[randomnum]) if randomnum > threshold else print("The number is lower than the threshold")
