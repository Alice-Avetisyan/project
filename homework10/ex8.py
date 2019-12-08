from multiprocessing import Process
numbers_list = [12, 32, 211, 43]


def even_position(numbers):
    for i in range(len(numbers)):
        if i % 2 == 0:
            numbers[i] += 2
    print(numbers)


def odd_position(numbers):
    for i in range(len(numbers)):
        if i % 2 != 0:
            numbers[i] *= 3
    print(numbers)


if __name__ == '__main__':
    p1 = Process(target=even_position, args=(numbers_list, ))
    p1.start()
    p1.join()

    p2 = Process(target=odd_position, args=(numbers_list, ))
    p2.start()
    p2.join()

    print("Processes are complete")
