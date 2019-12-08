from multiprocessing import Process
numbers_list = [12, 32, 211, 43]


def add(numbers):
    print("Add")
    for num in numbers:
        num += 100
        print(num)


def subtract(numbers):
    print("Subtract")
    for num in numbers:
        num -= 100
        print(num)


if __name__ == '__main__':
    p1 = Process(target=add, args=(numbers_list, ))
    p1.start()
    p1.join()

    p2 = Process(target=subtract, args=(numbers_list, ))
    p2.start()
    p2.join()

    print("Processes are complete")
