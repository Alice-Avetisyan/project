from functools import reduce
from multiprocessing import Process
numbers_list = [12, 32, 211, 43]


def sum(numbers):
    print(reduce(lambda x, y: x+y, numbers))


def even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    p1 = Process(target=sum, args=(numbers_list, ))
    p1.start()
    p1.join()

    p2 = Process(target=even, args=(numbers_list, ))
    p2.start()
    p2.join()

    print("Processes are complete")

